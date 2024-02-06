import os
import sys

import click

from dosei import Dosei
from dosei.importer import import_from_string, ImportFromStringError

dosei_config_init = "dosei_config:dosei"

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
        app: Dosei = import_from_string(dosei_config_init)
    except ImportFromStringError:
        raise click.ClickException(f"Couldn't find a dosei_config.py file in \"{os.getcwd()}\"")
    if app.command is None:
        raise click.ClickException('Command "run" not found.')
    os.system(app.command)


@cli.command()
def dev():
    try:
        app: Dosei = import_from_string(dosei_config_init)
    except ImportFromStringError:
        raise click.ClickException(f"Couldn't find a dosei_config.py file in \"{os.getcwd()}\"")
    if app.dev is None:
        raise click.ClickException('Command "dev" not found.')
    os.system(app.dev)


@cli.command()
def export():
    try:
        app: Dosei = import_from_string(dosei_config_init)
        return app.export()
    except ImportFromStringError:
        raise click.ClickException(f"Couldn't find a dosei_config.py file in \"{os.getcwd()}\"")
