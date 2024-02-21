"""Interact with folders in Nessus."""
import typer
from restfly.errors import RequestConflictError
from rich.console import Console
from rich.table import Table
from tenable.nessus import Nessus
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def list(ctx: typer.Context):
    """List all folders."""
    connection = ctx.obj.get("connection")

    folders = connection.folders.list()

    table = Table(title="All available folders")

    table.add_column("Name", justify="left", style="cyan", no_wrap=True)
    table.add_column("ID")
    table.add_column("Unread Count", justify="right")

    for folder in folders:
        table.add_row(folder["name"], str(folder["id"]), str(folder["unread_count"]))

    console = Console()
    console.print(table)


@app.command()
def create(
    ctx: typer.Context,
    folder_name: Annotated[
        str,
        typer.Option(help="Name of the folder to create", prompt=True),
    ],
):
    """Create a new folder."""
    connection = ctx.obj.get("connection")

    try:
        connection.folders.create(folder_name)
    except RequestConflictError:
        return

    for folder in connection.folders.list():
        if folder["name"] == folder_name:
            print(
                f'Folder {folder_name} has ID {folder["id"]} and was successfully created.'
            )
