#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Configuration tasks to be run after the template has been generated."""

import logging
import os
import shutil

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("post_gen_project")

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

DOCS_SOURCES = "docs_sources"
ALL_TEMP_FOLDERS = [DOCS_SOURCES]
DOCS_FILES_BY_TOOL = {
    "mkdocs": ["help.md", "/mkdocs.yml"],
    "sphinx": ["conf.py", "index.rst", "Makefile"],
}


def move_docs_files(docs_tool, docs_files, docs_sources) -> None:
    if docs_tool == "none":
        return

    root = os.getcwd()
    docs = "docs"

    logger.info("Initializing docs for %s", docs_tool)
    if not os.path.exists(docs):
        os.mkdir(docs)

    for item in docs_files[docs_tool]:
        dst, name = (root, item[1:]) if item.startswith("/") else (docs, item)
        src_path = os.path.join(docs_sources, docs_tool, name)
        dst_path = os.path.join(dst, name)

        logger.info("Moving %s to %s.", src_path, dst_path)
        if os.path.exists(dst_path):
            os.unlink(dst_path)

        os.rename(src_path, dst_path)


def remove_temp_folders(temp_folders) -> None:
    for folder in temp_folders:
        logger.info("Remove temporary folder: %s", folder)
        shutil.rmtree(folder)


def remove_cli_script(cli_enable: str, project_slug: str) -> None:
    print(cli_enable)
    print(os.listdir(f"src/{project_slug}"))
    if cli_enable == "none":
        os.remove(f"src/{project_slug}/cli.py")


def setup_git_repo() -> None:
    # Create git repo
    os.system("git init -q")
    # Setup empty main and dev
    os.system("git checkout --orphan main -q")
    os.system('git commit --allow-empty -m "Initial commit." -q')
    os.system("git checkout --orphan dev -q")
    os.system('git commit --allow-empty -m "Initial commit." -q')
    # Add cookiecutter on new branch
    os.system("git checkout -b cookiecutter -q")
    os.system("git add . ")
    os.system('git commit -am "Setup cookiecutter" -q')
    os.system('git tag -a v0.0.0 -m "Release tag for version 0.0.0"')


def setup_env() -> None:
    logger.info(INFO + "Creating conda environment..." + TERMINATOR)
    os.system(
        "conda env create " "--file environment.yml " "--name python{{cookiecutter.minimal_python_version}}",
    )

    logger.info(INFO + "Setting the virtual environment. This env can be used in all different taks." + TERMINATOR)
    logger.info(
        INFO
        + "Run conda activate python{{cookiecutter.minimal_python_version}} && cd {{cookiecutter.project_slug}} && make setup-all"
        + TERMINATOR,
    )
    logger.info(
        INFO + "Install direnv (visit https://direnv.net/docs/installation.html) and run direnv allow " + TERMINATOR,
    )


def main() -> None:

    project_slug = "{{ cookiecutter.project_slug }}"

    move_docs_files("{{cookiecutter.docs_tool}}", DOCS_FILES_BY_TOOL, DOCS_SOURCES)
    remove_temp_folders(ALL_TEMP_FOLDERS)
    remove_cli_script("{{cookiecutter.command_line_interface}}", project_slug)
    logger.info(
        SUCCESS + "Project initialized successfully! You can now jump to {} folder".format(project_slug) + TERMINATOR,
    )
    logger.info(INFO + "{}/README.md contains instructions on how to proceed.".format(project_slug) + TERMINATOR)
    setup_git_repo()
    setup_env()


if __name__ == "__main__":
    main()

# EOF
