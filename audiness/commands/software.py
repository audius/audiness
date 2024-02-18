"""Interact with scans in Nessus."""
import typer

app = typer.Typer()


@app.command()
def update(ctx: typer.Context):
    """Update Nessus."""
    connection = ctx.obj.get("connection")

    connection.software_update.update()    
