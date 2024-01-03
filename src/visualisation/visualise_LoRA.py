import matplotlib.pyplot as plt
import wandb


def visualise_and_save(exec_time, memory_usage):
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.set_xlabel("Run")
    ax1.set_ylabel("Execution Time (seconds)", color="tab:blue")
    ax1.plot(exec_time, color="tab:blue", marker="o", label="Execution Time")
    ax1.tick_params(axis="y", labelcolor="tab:blue")

    ax2 = ax1.twinx()

    ax2.set_ylabel("Memory Consumption (GB)", color="tab:red")
    ax2.plot(memory_usage, color="tab:red", marker="o", label="Memory Consumption")
    ax2.tick_params(axis="y", labelcolor="tab:red")

    fig.tight_layout()
    plt.title("Execution Time and Memory Consumption Over a Run")

    wandb.log({"plot_exec_time_and_memory": fig})
    plt.close()
