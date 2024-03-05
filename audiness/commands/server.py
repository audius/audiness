"""Interact with the Nessus instance."""

import typer
from rich.console import Console
from rich.progress import track
from rich.table import Table

from audiness.helpers import human_readable_datetime

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


@app.command()
def status(ctx: typer.Context):
    """Get the status of the Nessus instance."""
    connection = ctx.obj.get("connection")

    status = connection.settings.health()["perf_stats_history"]

    human_readable_datetime(status, "timestamp")

    table = Table(title="Status")

    table.add_column("Timestamp", justify="left", style="cyan", no_wrap=True)
    table.add_column("kBytes received")
    table.add_column("kBytes sent")
    table.add_column("Nessus RAM")

    for entry in status:
        table.add_row(
            entry["timestamp"],
            str(entry["kbytes_received"]),
            str(entry["kbytes_sent"]),
            str(entry["nessus_mem"]),
        )

    console = Console()
    console.print(table)
