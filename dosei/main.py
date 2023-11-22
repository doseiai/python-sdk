import sys

import click

from dosei import Dosei
from dosei.importer import import_from_string


@click.group()
def cli():
    pass


@cli.command()
@click.argument("func")
def run(func):
    sys.path.insert(0, "")
    Dosei.call_func(import_from_string(func))


@cli.command()
@click.argument("app")
def export(app):
    sys.path.insert(0, "")
    app: Dosei = import_from_string(app)
    return app.export()
