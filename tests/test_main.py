"""Tests for main part of audiness."""

from typer.testing import CliRunner

from audiness.main import app

runner = CliRunner()


def test_app1():
    """Test if the app raises an error when the access key is not provided."""
    result = runner.invoke(app, ["--access_key"], input="123456\n")
    assert result.exit_code == 2


def test_app2():
    """Test if the app raises an error when the secret key is not provided."""
    result = runner.invoke(app, ["--secret_key"], input=None)
    assert result.exit_code == 2


def test_app3():
    """Test if the app raises an error when the host URL is not provided."""
    result = runner.invoke(app, ["--host"], input="https://localhost:8834\n")
    assert result.exit_code == 2
