"""Helper elements for various tasks."""
from datetime import datetime

from tenable.nessus import Nessus


def setup_connection(host, access_key, secret_key):
    """Connect to the Nessus instance."""
    connection = Nessus(url=host, access_key=access_key, secret_key=secret_key)
    return connection


def human_readable_datetime(data, *args):
    """Replace timestamps with a human readable date in a dict."""
    format_string = "%Y-%m-%d %H:%M:%S"
    for entry in data:
        for element in args:
            entry[element] = datetime.fromtimestamp(entry[element]).strftime(
                format_string
            )

    return data
