from enum import Enum
from random import choice
from typing import Optional

import typer
from rich.console import Console


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="{{cookiecutter.project_slug}}",
    help="{{cookiecutter.description}}",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]{{ cookiecutter.project_slug }}[/] version: [bold blue]{__version__}[/]")
        raise typer.Exit()


@app.command(name="")
def main(
    name: str = typer.Option(..., help=""),
    color: Optional[Color] = typer.Option(
        None,
        "-c",
        "--color",
        "--colour",
        case_sensitive=False,
        help="Color for print. If not specified then choice will be random.",
    ),
) -> None:
    if color is None:
        color = choice(list(Color))

    console.print(f"[bold {color}][/]")


if __name__ == "__main__":
    app()
