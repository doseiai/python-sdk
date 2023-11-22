import sys

import click

from dosei import Dosei
from dosei.importer import import_from_string

# Add current dir to PYTHONPATH
sys.path.insert(0, "")


@click.group()
def cli():
    pass


@cli.command()
@click.argument("func")
def run(func):
    Dosei.call_func(import_from_string(func))


@cli.command()
@click.argument("app")
def export(app):
    app: Dosei = import_from_string(app)
    return app.export()
