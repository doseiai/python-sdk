import click

from dosei import Dosei
from dosei.importer import import_from_string


@click.command()
@click.argument("app")
def cli(app):
    Dosei.call_func(import_from_string(app))
