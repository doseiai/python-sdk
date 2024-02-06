import os
import subprocess
import sys

import click

from dosei import Dosei
from dosei.importer import import_from_string, ImportFromStringError

# Add current dir to PYTHONPATH
sys.path.insert(0, "")


@click.group()
def cli():
    pass


@cli.command()
@click.argument("func", required=False)
def run(func):
    if func:
        return Dosei.call_func(import_from_string(func))
    try:
        app: Dosei = import_from_string("dosei:dosei")
    except ImportFromStringError:
        raise click.ClickException(f"Couldn't find a dosei.py file in \"{os.getcwd()}\"")
    if app.dev is None:
        raise click.ClickException('Command "run" not found.')
    subprocess.check_call(app.command)


@cli.command()
def dev():
    try:
        app: Dosei = import_from_string("dosei:dosei")
    except ImportFromStringError:
        raise click.ClickException(f"Couldn't find a dosei.py file in \"{os.getcwd()}\"")
    if app.dev is None:
        raise click.ClickException('Command "dev" not found.')
    subprocess.check_call(app.dev)


@cli.command()
@click.argument("app")
def export(app):
    app: Dosei = import_from_string(app)
    return app.export()
