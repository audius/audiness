"""Interact with scans in Nessus."""

import io
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.progress import track
from rich.table import Table
from typing_extensions import Annotated

from audiness.helpers import human_readable_datetime

app = typer.Typer()


@app.command()
def list(ctx: typer.Context):
    """List all available scans."""
    connection = ctx.obj.get("connection")
    scans = connection.scans.list()["scans"]

    human_readable_datetime(scans, "creation_date", "last_modification_date")

    table = Table(title="All available scans")

    table.add_column("Name", justify="left", style="cyan", no_wrap=True)
    table.add_column("ID")
    table.add_column("Last modification date")
    table.add_column("Status")
    table.add_column("Folder ID")

    for scan in scans:
        table.add_row(
            scan["name"],
            str(scan["id"]),
            scan["last_modification_date"],
            scan["status"],
            str(scan["folder_id"]),
        )

    console = Console()
    console.print(table)


@app.command()
def export(
    ctx: typer.Context,
    identifier: Annotated[
        str, typer.Option(help="String for the identification", prompt=True)
    ] = "SAS",
    path: Annotated[
        Optional[Path],
        typer.Option(help="Path to store the exported files", prompt=True),
    ] = ".",
    history_max: Annotated[
        int,
        typer.Option(help="Number for bulk download scans from 1 to given value", prompt=True),
    ] = 1,
):
    """Export a Nessus scan or Nessus scans."""
    connection = ctx.obj.get("connection")

    # Get all scans
    scans = connection.scans.list()

    # Clean scans result and limit data to what's needed
    del scans["timestamp"]
    del scans["folders"]

    failed_exports = []
    relevant_scans = []

    for scan in scans["scans"]:
        if scan["name"].startswith(identifier) and scan["status"] == "completed":
            relevant_scans.append(scan)

    # Downloads all files in given history
    for act_history in range(1, history_max + 1):

        # Export all scans which matches the identifier
        for scan in track(relevant_scans, description="Processing scans ..."):
            scan_history = connection.scans.details(scan["id"])["history"]

            try:
                single_scan = scan_history[-abs(act_history)]

                short_date = datetime.fromtimestamp(
                    single_scan["last_modification_date"]
                ).strftime("%Y%m%d_%H%M%S")
                historic_scan_id = single_scan["history_id"]

                filename = Path(path) / Path(f'{scan["name"]}_{short_date}.nessus')

                scan_data = connection.scans.export_scan(
                    scan_id=scan["id"], history_id=historic_scan_id, format="nessus"
                )
                Path(filename).write_bytes(scan_data.getbuffer())
            except IndexError:
                failed_exports.append(scan["name"])

        print(
            f"{len(relevant_scans)} files selected, {len(relevant_scans)-len(failed_exports)} exported, {len(failed_exports)} failed."
        )
        if failed_exports:
            print(f"Failed exports:")
            for element in failed_exports:
                print(element)
