def load_data_to_fine_tune():
    """Load the dataset and filter for Python language."""
    dtypes_questions = {"Id": "int32", "Score": "int16", "Title": "str", "Body": "str"}
    df_questions = pd.read_csv(
        "Questions.csv",
        usecols=["Id", "Score", "Title", "Body"],
        encoding="ISO-8859-1",
        dtype=dtypes_questions,
    )

    dtypes_answers = {
        "Id": "int32",
        "ParentId": "int32",
        "Score": "int16",
        "Body": "str",
    }
    df_answers = pd.read_csv(
        "Answers.csv",
        usecols=["Id", "ParentId", "Score", "Body"],
        encoding="ISO-8859-1",
        dtype=dtypes_answers,
    )

    merged = pd.merge(df_questions, df_answers, left_on="Id", right_on="ParentId", how="inner")
    # Sort by score of the answer in descending order and drop duplicates based on question ID
    merged = merged.sort_values(by="Score_y", ascending=False).drop_duplicates(subset="Id_x", keep="first")

    # Remove HTML tags using BeautifulSoup
    merged["Body_x"] = merged["Body_x"].apply(lambda x: BeautifulSoup(x, "lxml").get_text())
    merged["Body_y"] = merged["Body_y"].apply(lambda x: BeautifulSoup(x, "lxml").get_text())

    merged["combined_question"] = merged["Title"] + ": " + merged["Body_x"]

    # Rename and select the desired columns
    final_df = merged[["Score_x", "Score_y", "combined_question", "Body_y"]]
    final_df.columns = ["score_question", "score_answer", "question", "answer"]

    final_df = final_df[(final_df["score_question"] >= 0) & (final_df["score_answer"] >= 0)]

    # Contains code that resembles python code
    final_df = final_df[final_df["question"].apply(contains_code) | final_df["answer"].apply(contains_code)]

    return final_df
