"""Interact with the Nessus instance."""

import typer
from rich.console import Console
from rich.progress import track
from rich.table import Table

app = typer.Typer()


@app.command()
def status(ctx: typer.Context):
    """Get the status of the Nessus instance."""
    connection = ctx.obj.get("connection")

    status = connection.server.status()

    print(status)


@app.command()
def alerts(ctx: typer.Context):
    """Get the alerts of the Nessus instance."""
    connection = ctx.obj.get("connection")

    alerts = connection.settings.alerts()

    table = Table(title="Alerts")

    table.add_column("Alert", justify="left", style="cyan", no_wrap=True)
    table.add_column("Description")
    table.add_column("Type")
    table.add_column("Severity")

    for alert in alerts:
        table.add_row(
            alert["alert"],
            alert["description"],
            alert["type"],
            str(alert["severity"]),
        )

    console = Console()
    console.print(table)
