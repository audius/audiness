"""Interact with policies in Nessus."""

import typer
from rich.console import Console
from rich.table import Table
from tenable.nessus import Nessus

from audiness.helpers import human_readable_datetime

app = typer.Typer()


@app.command()
def list(ctx: typer.Context):
    """List all policies."""
    connection = ctx.obj.get("connection")

    policies = connection.policies.list()

    human_readable_datetime(policies, "last_modification_date", "creation_date")

    table = Table(title="All available policies")

    table.add_column("Name", justify="left", style="cyan", no_wrap=True)
    table.add_column("Description")
    table.add_column("Creation date")
    table.add_column("Last modification date")

    for policy in policies:
        table.add_row(
            policy["name"],
            policy["description"],
            policy["creation_date"],
            policy["last_modification_date"],
        )

    console = Console()
    console.print(table)
