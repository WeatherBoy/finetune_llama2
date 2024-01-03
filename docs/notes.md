# General Notes
## Fine-tuning Llama2
### Practical approach
#### Meta's own documentation
This is Meta's own documentation and it is a really good ressource for using Llama 2, [LINK](https://ai.meta.com/llama/get-started/).

Furtehremore, there is this specific section on ressources which looks really good! [LINK](https://ai.meta.com/llama/get-started/#:~:text=issues%20using%20Asana.-,Resources,-Github).

#### Medium
A very good Medium article: [How to Fine-Tune Llama2 for Python Coding on Consumer Hardware
](https://towardsdatascience.com/how-to-fine-tune-llama2-for-python-coding-on-consumer-hardware-46942fa3cf92).

#### Weights & Biases
Maybe `WandB` has some good tips and tricks for how to fine-tune an LLM: [Training and Fine-tuning Large Language Models (LLMs)](https://www.wandb.courses/courses/take/training-fine-tuning-LLMs/lessons/48864885-course-introduction)


#### PEFT
Should one write something about [State-of-the-art Parameter-Efficient Fine-Tuning (PEFT) methods](https://github.com/huggingface/peft), cause I'm quite certain that I'm using it in the code.

### Theoretical approach
#### LoRA
Look at and read this paper:
Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., & Chen, W. (2021). LoRA: Low-Rank Adaptation of Large Language Models. arXiv preprint arXiv:2106.09685

#### QLoRA
Look at and read this paper:
Dettmers, T., Pagnoni, A., Holtzman, A., & Zettlemoyer, L. (2023). QLoRA: Efficient Finetuning of Quantized LLMs. arXiv preprint arXiv:2305.14314.


## MLOps
### CookieCutter
Nikki is the GOAT. When in doubt just look at his [MLOps repository](https://github.com/SkafteNicki/mlops_template/tree/master)!

### Hydra
If you have loaded your configuration file with **Hydra** then you can print the *configurations* (to check whether it works) as:
```
import hydra
from omegaconf import OmegaConf

@hydra.main(config_path="../conf", config_name="config", version_base="1.2")
def main(cfg):
    print(OmegaConf.to_yaml(cfg))
```
Just make sure the path and naming conventions are correct.

## Prompt engineering
### Principled Instructions Are All You Need
There is this really good [paper](https://arxiv.org/pdf/2312.16171.pdf) on prompt engineering, that details some different "prompt principles", which should significantly enhance the performance given your prompts.
([Link to HuggingFace](https://huggingface.co/papers/2312.16171)).
