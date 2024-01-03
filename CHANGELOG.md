# CHANGELOG



## v0.2.0 (2024-01-03)

### :bug:

* :bug: `all_param` -&gt; `all_params` ([`da8f226`](https://github.com/WeatherBoy/finetune_llama2/commit/da8f2265ad6319f95ff99c123887fe752330b490))

* :bug: kinda fixed a bug in the sense that I forgot to paste the content of `load_data_to_finetune.py` ([`f9acae8`](https://github.com/WeatherBoy/finetune_llama2/commit/f9acae8ea1f0df254dbcf3374520c279ce37fae0))

* :bug: put project structure in code env ([`32bd47d`](https://github.com/WeatherBoy/finetune_llama2/commit/32bd47d2683c7728bca5f8c4a90c4448ca58aa07))

### :fire:

* :fire: delete HugginFace *functions* and *params* ([`ba4a250`](https://github.com/WeatherBoy/finetune_llama2/commit/ba4a250a45e491e008567406bdb0f8875f2a3887))

### Other

* :twisted_rightwards_arrows: Merge pull request #9 from WeatherBoy/2-pick-and-configure-a-logger

2 pick and configure a logger ([`959bbc1`](https://github.com/WeatherBoy/finetune_llama2/commit/959bbc19652b6fc2e6aebce68e015f346c95ef5d))

* :package: `import pandas` ([`8f1241a`](https://github.com/WeatherBoy/finetune_llama2/commit/8f1241a439799a729c5bb72a196f757ada8202c2))

* :construction: `import load_data_to_finetune` ([`6683cb0`](https://github.com/WeatherBoy/finetune_llama2/commit/6683cb00ce4a07fc0fb2dc3b5cbdd0851d113427))

* :coffin: :bulb: comment out unnecessary code ([`a1e68c5`](https://github.com/WeatherBoy/finetune_llama2/commit/a1e68c51ebef4c45cace5a8d4e50934bab29a0a2))

* :coffin: remove unused packages ([`a5dc50a`](https://github.com/WeatherBoy/finetune_llama2/commit/a5dc50a61fe714e7c7434f384d20ee6d12cdfb14))

* :twisted_rightwards_arrows: Merge branch &#39;2-pick-and-configure-a-logger&#39; of https://github.com/WeatherBoy/finetune_llama2 into 2-pick-and-configure-a-logger ([`f8a54a3`](https://github.com/WeatherBoy/finetune_llama2/commit/f8a54a3d19b383d4ff55c59b9946adfee4777e1f))

* :see_no_evil: add `__pycache__` to `.gitignore` ([`443cdd4`](https://github.com/WeatherBoy/finetune_llama2/commit/443cdd453dbf7a2f56a5c87c418283f80c91c705))

* :twisted_rightwards_arrows: Merge pull request #8 from WeatherBoy/configure-config

Configure config ([`2d320c6`](https://github.com/WeatherBoy/finetune_llama2/commit/2d320c67ae844ef2d1dce285c8efb8cfc2c9be32))

* :pencil2: `all_param` -&gt; `all_params` ([`fee33d6`](https://github.com/WeatherBoy/finetune_llama2/commit/fee33d64c64547071420b120e0d4eabfd4e381ba))

* :pencil: `print_trainable..` -&gt; `log_trainable..` ([`be060a2`](https://github.com/WeatherBoy/finetune_llama2/commit/be060a201a48138be8fa28068d0eff9b206a1cf2))

* :truck: move `load_data_to_finetune` ([`dbe82b5`](https://github.com/WeatherBoy/finetune_llama2/commit/dbe82b5994c596ff30784f453d6564449e31f248))

* :recycle: update name of *function* for loading **Hydra** configs ([`e23fe42`](https://github.com/WeatherBoy/finetune_llama2/commit/e23fe4251f10fa573e682c0288def89f0a667fba))

* :recycle: refactor imports with regards to renaming ([`b4bc240`](https://github.com/WeatherBoy/finetune_llama2/commit/b4bc240c2564d6be4b6b51c63eee8ceb31f44a35))

* :loud_sound: update `print_trainable_parameters( )` with `wandb` ([`b7821fa`](https://github.com/WeatherBoy/finetune_llama2/commit/b7821fa0b3a50bfd25cb70fa85da8da16e6be746))

* :wrench: update config paths to project structure ([`a8015be`](https://github.com/WeatherBoy/finetune_llama2/commit/a8015be44afea6d38bcd182f2f6748a79f75f977))

* :truck: rename to specific fine-tune method ([`bbf9c7d`](https://github.com/WeatherBoy/finetune_llama2/commit/bbf9c7dfb0a41f5bbf50ca9cace52ae3abdbfdd6))

* :coffin: remove `max_length` from `generate_code_from_prompt( )`

As I also wrote in a comment: I think it was unwise to introduce it at all, so instead of giving myself a headache later I just elected to remove it again. ([`d128815`](https://github.com/WeatherBoy/finetune_llama2/commit/d128815922dabb424f9e8bae301681098723db6f))

* :truck: rename files to *Llama2* specific ([`7fc5e78`](https://github.com/WeatherBoy/finetune_llama2/commit/7fc5e7848e36bab42addfe4be9630bdf926048fa))

* :construction: update `fine_tune.py` ([`d9418d3`](https://github.com/WeatherBoy/finetune_llama2/commit/d9418d323abe5960f80679512279e248cd774be2))

* :construction: add `wandb` to `visualise_and_save( )` ([`de261e9`](https://github.com/WeatherBoy/finetune_llama2/commit/de261e959dd0c357c147a1a8c786f9e4d12d4001))

* :memo: update `notes.md`

A little about Hydra and the Prompt engineering paper that Uffe shared. ([`9e73288`](https://github.com/WeatherBoy/finetune_llama2/commit/9e73288f11f063de282e03f0184ec887dbdcc4c7))

* :coffin: delete unnecessary imports ([`8b5c02f`](https://github.com/WeatherBoy/finetune_llama2/commit/8b5c02faa458e7876691a2144b4c904dc7716b7c))

* :recycle: data handling goes to data handling DIR ([`f95d5f9`](https://github.com/WeatherBoy/finetune_llama2/commit/f95d5f9d9076c408662f5745a30fae96ededb28e))

* :construction: update `generate_code_from_prompt( )` a little

I added an extra function parameter and I updated the function documentation. ([`a80e3ee`](https://github.com/WeatherBoy/finetune_llama2/commit/a80e3ee87f826491d639d732f710a821967a89d2))

* :truck: rename `visualisation.py` -&gt; `visualise_llama2.py` ([`e464ba2`](https://github.com/WeatherBoy/finetune_llama2/commit/e464ba2f36eb9e2a7c2c6e4a238d0eb62340fa26))

* :coffin: remove code designed for previous dataset ([`0ded84b`](https://github.com/WeatherBoy/finetune_llama2/commit/0ded84bcf499b64f7aa306e377def3dc0a165b2d))

* :pencil2: &#34;visualize&#34; -&gt; &#34;visualise&#34; ([`f89d7e9`](https://github.com/WeatherBoy/finetune_llama2/commit/f89d7e9a3dd5cb667cfc4298cb1ca63bdc1280d6))

* :recycle: update `fine_tune_llama2.py` A LOT!

Using *Weights and Biases* for the configuration (even though I still am a bit janky at this). Then I also removed the `visualize_and_save( )` function to a `visualisation.py` script. ([`19d2535`](https://github.com/WeatherBoy/finetune_llama2/commit/19d2535082a32259d575e0629893a2f2ce6a200a))

* :recycle: add `visualisation.py` script ([`4e95505`](https://github.com/WeatherBoy/finetune_llama2/commit/4e95505d42caa8cfcccb278db6f6e1472f2032be))

* :wrench: `hydra` might just work now ([`8ade598`](https://github.com/WeatherBoy/finetune_llama2/commit/8ade59811939cf94a9a8ad34e9669d587295e8d6))

* :construction: print hyperparameters nicely ([`e960e4f`](https://github.com/WeatherBoy/finetune_llama2/commit/e960e4f104494e378951d39f95aebe677f8b5b7a))

* :wrench: add *base* `hydra`-version to config files ([`db79f69`](https://github.com/WeatherBoy/finetune_llama2/commit/db79f699e8d0bdfd8a015aff46d11eb6dcbf7b11))

* :construction: move `load_data_to_fine_tune( )`  *(for now)* ([`340af37`](https://github.com/WeatherBoy/finetune_llama2/commit/340af3789ecdea1645cc61189d2c726ad9600b4a))

* :construction: test run of `hydra` ([`7e19825`](https://github.com/WeatherBoy/finetune_llama2/commit/7e1982588c90b2239953c948e7cb864a45498a1d))

* :see_no_evil: add `pycache` to `.gitignore` ([`f66b20c`](https://github.com/WeatherBoy/finetune_llama2/commit/f66b20c16df46c6f78ac37b245a855301a2579c9))

* :wrench: actually update configuration files

Added a configuration directory and added the hyperparameters in there ([`7029df1`](https://github.com/WeatherBoy/finetune_llama2/commit/7029df123c9cc00549fcc36d4edc541789a37e3a))

* :construction: add `__init__.py` to `/src` ([`68a4638`](https://github.com/WeatherBoy/finetune_llama2/commit/68a4638795cfaf851f1f7bfa7aa9ecaa3286190f))

* :construction: refactor setup - intermediate ([`ac53d4b`](https://github.com/WeatherBoy/finetune_llama2/commit/ac53d4b8d8ef329decdd3871e1c174008ced7d44))

* :memo: add `peft` and `WandB` to `notes.md` ([`f6f38c8`](https://github.com/WeatherBoy/finetune_llama2/commit/f6f38c89a930351e19d3ce21f15ac8bc1b30a7d3))

* :memo: add (no) information on `cookiecutter` ([`5cd48cb`](https://github.com/WeatherBoy/finetune_llama2/commit/5cd48cb83fde6fdb892e69d8fac04b9f0e0495b1))

* :twisted_rightwards_arrows: Merge pull request #6 from WeatherBoy/1-wrench-setup-and-understand-cookiecutter

1 wrench setup and understand cookiecutter ([`a9020d9`](https://github.com/WeatherBoy/finetune_llama2/commit/a9020d9d9ca6abdb9f1b16dbc181f63809af959f))

* Merge branch &#39;main&#39; into 1-wrench-setup-and-understand-cookiecutter ([`21fe4a4`](https://github.com/WeatherBoy/finetune_llama2/commit/21fe4a45dfa3aea8071f194123e04bf4fd5a95dc))

* :memo: add project structure to `README.md` ([`38bec1d`](https://github.com/WeatherBoy/finetune_llama2/commit/38bec1d0a5c3834784ca795435b5d1ae20ff5b26))

* :see_no_evil: add /data and /models to `.gitignore` ([`0ac4df9`](https://github.com/WeatherBoy/finetune_llama2/commit/0ac4df9760da11ee7b4fcccda7350d0c3ab7062c))

* :recycle: try to follow Nikki&#39;s CC structure

I&#39;ve tried to refactor my repository, such that it follows the structure of Nikki&#39;s `cookiecutter` (CC) template.
https://github.com/SkafteNicki/mlops_template/tree/master ([`a1328ec`](https://github.com/WeatherBoy/finetune_llama2/commit/a1328ec88baad55aa92621edf49fe77b3c617eae))

* :wrench: add `requirements_tests.txt` ([`dba91bd`](https://github.com/WeatherBoy/finetune_llama2/commit/dba91bd17c14033eeeee7da7ebf8806af1e2e70d))


## v0.1.0 (2023-12-20)

### :sparkles:

* :sparkles: initialise a general notes `.md` file ([`3d8b80b`](https://github.com/WeatherBoy/finetune_llama2/commit/3d8b80bc013c0f99b49a27217a270b047c687456))

### Other

* :twisted_rightwards_arrows: Merge pull request #5 from WeatherBoy/4-continuous-integration-flake8-and-isort

4 continuous integration flake8 and isort ([`bba93b9`](https://github.com/WeatherBoy/finetune_llama2/commit/bba93b9e25b4367e031c0ed4207c0e9f936c95b9))

* :heavy_minus_sign: remove `torch` from `requirements.txt`

I kinda didn&#39;t factor in that everytime I run a check now the poor GitHub node has to install `torch`... not smart ([`4b127df`](https://github.com/WeatherBoy/finetune_llama2/commit/4b127df0dc449913e4fad87a7515755c080b1867))

* :wrench: add an (initial) `requirements.txt` ([`58c3f34`](https://github.com/WeatherBoy/finetune_llama2/commit/58c3f34ed6d3b87affdec62551407d0ac83108fe))

* :art: ran `isort` and `flake8` ([`518e959`](https://github.com/WeatherBoy/finetune_llama2/commit/518e959611151d3c3517207a0ecd0342b02a614a))

* :construction_worker: add `flake8` and ignore VENV

Added a `flake8` GitHub action and also ignore the virtual environment. ([`5bd468b`](https://github.com/WeatherBoy/finetune_llama2/commit/5bd468ba1e45c852162f096227335c57da67960b))

* :construction_worker: add `isort` CI and ignore VENV

Added a `isort` GitHub action and I also ignore the virtual environment, which I this time have placed directly in the directory ([`88cf42d`](https://github.com/WeatherBoy/finetune_llama2/commit/88cf42d2b0871c5241eb86165d9b1977b5a2f9e0))

* :see_no_evil: add VENV to `.gitignore` (again) ([`5f34c97`](https://github.com/WeatherBoy/finetune_llama2/commit/5f34c97541ddef9d6c0ac59118e0d75e541d70b1))

* :see_no_evil: add virtual environment to `.gitignore` ([`b974033`](https://github.com/WeatherBoy/finetune_llama2/commit/b974033fc710266089b9fffb324d9d0e523e42d4))

* :memo: Update structure of `notes.md` ([`f68b33f`](https://github.com/WeatherBoy/finetune_llama2/commit/f68b33fa94387b19b361a937262c7a677afa2108))

* :construction: add files from *luisroque* repository ([`f21e4eb`](https://github.com/WeatherBoy/finetune_llama2/commit/f21e4ebb126855c58ff64e5d5f57491583791f31))

* :memo: updates `notes.md` ([`c6bf66c`](https://github.com/WeatherBoy/finetune_llama2/commit/c6bf66cae99e4a4c27641a0858fa10a41e776548))

* :construction_worker: add ASV ([`88a6c59`](https://github.com/WeatherBoy/finetune_llama2/commit/88a6c590c1a22f7dceb4fa9e13fdebc89397d58c))

* :pencil2: &#34;Elder&#34; -&gt; &#34;elder&#34;

Fixed capitalisation of &#34;elder&#34;. ([`ca18c06`](https://github.com/WeatherBoy/finetune_llama2/commit/ca18c06902fd548471164ad19e20211251c9f80d))

* :memo: update `README.md` ([`4433346`](https://github.com/WeatherBoy/finetune_llama2/commit/443334636d4a36991b14a9bed2d44b8fb683b043))

* :tada: initialise repository ([`9c1c8f1`](https://github.com/WeatherBoy/finetune_llama2/commit/9c1c8f108510893ddb976e06105266e102eba9b3))
