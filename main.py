"""Main part of audiness."""
import typer
from typing_extensions import Annotated

from commands import folders, scans, server, software
from helpers import setup_connection

app = typer.Typer()

app.add_typer(folders.app, name="folders")
app.add_typer(scans.app, name="scans")
app.add_typer(server.app, name="server")
app.add_typer(software.app, name="software")


@app.callback()
def main(
    ctx: typer.Context,
    access_key: Annotated[
        str,
        typer.Option(envvar="ACCESS_KEY", help="Nessus API access key", prompt=True),
    ],
    secret_key: Annotated[
        str,
        typer.Option(envvar="SECRET_KEY", help="Nessus API secret key", prompt=True),
    ],
    host: Annotated[
        str, typer.Option(help="URL to Nessus instance")
    ] = "https://localhost:8834",
):
    connection = setup_connection(host, access_key, secret_key)
    ctx.obj = {"connection": connection}


if __name__ == "__main__":
    app()
