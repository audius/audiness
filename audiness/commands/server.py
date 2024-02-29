"""Interact with the Nessus instance."""
import typer

app = typer.Typer()


@app.command()
def status(ctx: typer.Context):
    """Get the status of the Nessus instance."""
    connection = ctx.obj.get("connection")

    status = connection.server.status()

    print(status)
