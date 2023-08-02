[![made-with-python](https://img.shields.io/badge/Made%20with-Python-red.svg)](#python)

# Machine Learning Cookiecutter

This project template combines simplicity, best practice for folder structure and good OOP design.
The main idea is that there's much same stuff you do every time when you start your machine learning project, so
wrapping all this shared stuff will help you to change just the core idea every time you start a new project.

So, here’s a simple template that help you get into your main project faster and just focus on your core
(Model Architecture, Training Flow, etc.).

Once generated, the package skeletons have the following features:

- Good base folder structure for many kinds of ML Projects (see below);
- Using `conda` format to manage virtual environments and dependencies;
- Testing setup with `pytest` with `coverage` plugin;
- Type checks with [`mypy`](https://mypy.readthedocs.io);
- Docstring checks with [`darglint`](https://github.com/terrencepreilly/darglint);
- Security checks with [`safety`](https://github.com/pyupio/safety) and [`bandit`](https://github.com/PyCQA/bandit);
- Ready-to-use [`pre-commit`](https://pre-commit.com) hooks with code-formatting and security features;
- Ready-to-use `.editorconfig`, `.dockerignore`, `.gitignore` and `.gitattributes`. You don't have to worry about those things;
- Ready-to-use `.dvc/config` for Data Version Control;
- Documentation with [`MkDocs`](https://www.mkdocs.org) and plugins [`Material Design theme`](https://github.com/squidfunk/mkdocs-material),
  [`mkdocstrings`](https://github.com/pawamoy/mkdocstrings) or [`Sphynx`](https://www.sphinx-doc.org/en/master)
- Docstring coverage with [`interrogate`](https://github.com/econchick/interrogate);
- [`Hydra`](https://github.com/facebookresearch/hydra) config templates for elegantly configuring complex applications.
- [Conventional Commits](https://www.conventionalcommits.org/) enforcement with [`commitizen`](https://commitizen-tools.github.io/commitizen/).
- Optional [`Typer`](https://typer.tiangolo.com) CLI template to get you started quickly .

## Introduction

The objective of this project is to provide a generic machine learning template for python based projects.
This includes folder structure, testing and documentation tools which should work well for most small to midsize
(in terms of number of features & examples) projects using a single instance of a machine.

### Requirements to use the cookiecutter template:

- Anaconda (or miniconda)
- Python 3.6+  (we use f-strings. So should you)
- GNU make
- GNU sed
- [direnv](https://github.com/direnv/direnv)
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0:
  This can be installed with pip by or conda depending on how you manage your Python packages:

once you've installed anaconda, you can install the remaining requirements (including cookiecutter) by doing:

```bash
$ pip3 install -r requirements.txt
```

or

```bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

### To start a new project, run:

Generate a data science project from this template:

```
cookiecutter https://github.com/caetas/CookieCutter.git
```

Follow the prompts; if you are asked to re-download the cookiecutter template, input `yes`.
Default responses are shown in the squared brackets; to use them, leave your response blank, and press enter.

After creating the project, you should follow a couple of steps to make sure everything works automagically. Run the following
command after the generated `coookicutter` project template. The new version automatically does the following:

```
cd <repo_name>
git remote add origin <repo_ssh>
git push --all
git push origin --tags
git checkout main
git merge cookiecutter
git push --set-upstream origin main
```
**You can delete the other branches if you wish.**
Head over to the generated README.md file to read about the next steps and a more in-depth explanation of the generated project's
features.

### Input variables

Template generator will ask you to fill some variables.

The input variables, with their default values:

|     **Parameter**     |      **Default value**      | **Description**                                                                                                                                                               |
|:---------------------:|:---------------------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project_name`           | `project_name`              | Project Name. Needs to match the name of the project in bitbucket|
| `repo_name`              | `repo_name`                 | Repository Name. Needs to match the name of the repo in bitbucket |
| `description`            | based on the `project_name` | Brief description of your project. |
| `organization`           | based on the `project_name` | Name of the organization. We need to generate LICENCE and to specify ownership in `pyproject.toml`. |
| `license`                | `MIT`                       | One of `MIT`, `BSD-3`, `GNU GPL v3.0` and `Apache Software License 2.0`. |
| `minimal_python_version` | `3.7`                       | Minimal Python version. One of `3.7`, `3.8` and `3.9`. It is used for builds and formatters (`black`, `isort` and `pyupgrade`). |
| `organization_email`     | based on the `organization` | Email for `SECURITY.md` files and to specify the ownership of the project in `pyproject.toml`. |
| `version`                | `0.0.0`                     | Initial version of the package. Make sure it follows the [Semantic Versions](https://semver.org) specification. |
| `line_length`            | 120                         | The max length per line (used for codestyle with `black` and `isort`). NOTE: This value must be between 50 and 140. |
| `command_line_interface` | `none`                      | If `typer` is chosen generator will create simple CLI application with [`Typer`](https://github.com/tiangolo/typer) library. |

### The resulting directory structure

The directory structure of your new project looks like this:

```
├── README.md          <- The top-level README for developers using this project.
├── AUTHORS.md         <- List of contributors
├── LICENSE
├── VERSION.txt        <- Version of the project
│
├── Makefile           <- Build configuration (uses GNU make). Type `make help` to see all available commands.
│
├── .dvc
│   └── config         <- DVC configuration file
│
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump from demdata
│       └── *.dvc      <- DVC metadata files
│
├── docs               <- A default Sphinx/Mkdocs project
│   ├── CONTRIBUTING.md
│   ├── DEVELOPER.md
│   ├── LOADING_ENV_VARIABLES.md
│   └── SECURITY.md
│
├── configs            <- Hydra compositional config
│   ├── config.yaml    <- current experiment configuration
│   ├── logger
│   ├── modelq
│   ├── optimizer
│   └── dataset
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│                         compiled model .pkl or HDFS (.h5) or .pb format (also available on Minio Server)
│  
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration.ipynb`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements  
│   ├── requirements.txt      <- The requirements file for reproducing the model analysis environment, e.g. generated with `pip freeze > requirements.txt`
│   ├── requirements-dev.txt  <- The requirements file for code formatting and anlysis.
│   ├── requirements-note.txt <- The requirements file for reproducing the analysis environment using jupyter notebook.
│   ├── requirements-dempy.txt<- The requirements file for installing dempy.
│   └── requirements-docs.txt <- The requirements file for building the project's documentation.  
│
├── .gitignore         <- A gitignore file specifies intentionally un-tracked files that Git should ignore.
├── .dvcignore         <- A dvcignore file specifies intentionally un-tracked files that DVC should ignore.
├── .dockerignore      <- Files / folders to be ignored for Docker build.
├── .envrc             <- Example .envrc file with environment for local development experience.
├── .secrets           <- Secrets and credentials should be stored here as environmental variables.
├── .flake8
├── .editorconfig
├── .pre-commit-config.yaml <- Configuration of automatic code formatting.
│
├── MODEL_CARD.md      <- Model cards are markdown files that accompany the models and provide very useful information.
│
├── pyproject.toml     <- Configuration file for several dev tools such as black, isort, mypy, coverage
│
├── logs               <- Logs generated by Hydra/Tensorboard and Trainer loggers
├── test               <- directory with your tests
│
├── scripts  
│   ├── bump_version.sh
│   ├── hadolint.sh
│   ├── nbconverter.sh  
│   └── shellcheck.sh
│
├── src/{{cookiecutter.project_slug}}  <- Source code for use in this project.
│   ├── __init__.py    <- Makes src/{{cookiecutter.project_slug}} a python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │
│   ├── utils          <- Utility scripts
│   │
│   ├── models         <- Scripts to store model architectures
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│
└── environment.yml <- file with libraries and library versions for recreating the analysis environment with conda.
```

## Contributing

Any contributions are welcome including improving the template and example projects.

### Submit a Pull Request

Pull requests are welcome, if they're small, atomic, and if they make my own packaging experience better.

### Installing development requirements

```
pip3 install -r requirements.txt
```

## Credits

This template is heavily based on [PyPackage](https://github.com/audreyr/cookiecutter-pypackage) template from
[@audreyr](https://github.com/audreyr).

It is also inspired by:

- [Data Science](https://github.com/drivendata/cookiecutter-data-science) template from [Driven Data](http://drivendata.github.io/cookiecutter-data-science/).
- [Python Best Practices Cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter)
- [python-package-template](https://github.com/TezRomacH/python-package-template)
- [AWS mlmax](https://github.com/awslabs/mlmax)
- [AWS python-data-science-template](https://github.com/aws-samples/python-data-science-template)
- [Microsoft MLOpsPython](https://github.com/microsoft/MLOpsPython)
- [Databrickslabs cicd-templates](https://github.com/databrickslabs/cicd-templates)
- [EasyData](https://github.com/hackalog/easydata)
- [pyscaffoldext-dsproject](https://github.com/pyscaffold/pyscaffoldext-dsproject)
- [MaD Cookiecutter](https://github.com/mad-lab-fau/mad-cookiecutter)
- [nestauk/ds-cookiecutter](https://github.com/nestauk/ds-cookiecutter)
- [GokuMohandas/MLOps](https://github.com/GokuMohandas/MLOps)
- [nielstiben/MLOPS-Project](https://github.com/nielstiben/MLOPS-Project)
- [Kedro](https://github.com/kedro-org/kedro)
- [best-practice-and-impact/govcookiecutter](https://github.com/best-practice-and-impact/govcookiecutter)

This template was inspired by several great articles:

- [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup)

## License

You can check out the full license [here](LICENSE.md)

This project is licensed under the terms of the [MIT](https://choosealicense.com/licenses/mit) license.
