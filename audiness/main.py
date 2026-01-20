"""Main part of audiness."""
import typer
from typing_extensions import Annotated
from validators import url

from audiness.commands import folders, policies, scans, server, software
from audiness.helpers import setup_connection

app = typer.Typer()

app.add_typer(folders.app, name="folders")
app.add_typer(policies.app, name="policies")
app.add_typer(scans.app, name="scans")
app.add_typer(server.app, name="server")
app.add_typer(software.app, name="software")


def validate_host(value: str):
    """Check if host is a valid URL."""
    if url(value):
        raise typer.BadParameter("URL is not valid")
    return value


def validate_key(value: str):
    """Check the length of an API key."""
    if len(value) != 64:
        raise typer.BadParameter("Key doesn't have the right length")
    return value


@app.callback()
def main(
    ctx: typer.Context,
    access_key: Annotated[
        str,
        typer.Option(
            envvar="ACCESS_KEY",
            help="Nessus API access key",
            prompt=True,
            callback=validate_key,
        ),
    ],
    secret_key: Annotated[
        str,
        typer.Option(
            envvar="SECRET_KEY",
            help="Nessus API secret key",
            prompt=True,
            callback=validate_key,
        ),
    ],
    host_url: Annotated[
        str,
        typer.Option(
            envvar="HOST_URL",
            help="URL to Nessus instance",
            prompt=True,
            callback=validate_host,
        ),
        ],
    # host: Annotated[
    #     str, typer.Option(help="URL to Nessus instance", callback=validate_host)
    # ] = "https://localhost:8838",
):
    connection = setup_connection(host_url, access_key, secret_key)
    ctx.obj = {"connection": connection}


if __name__ == "__main__":
    app()
