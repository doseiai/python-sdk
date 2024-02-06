import os
import sys

from dosei import Dosei
from dosei.importer import import_from_string, ImportFromStringError

dosei_config_init = "dosei_config:dosei"

# Add current dir to PYTHONPATH
sys.path.insert(0, "")


def run(func):
    if func:
        return Dosei.call_func(import_from_string(func))
    try:
        app: Dosei = import_from_string(dosei_config_init)
    except ImportFromStringError:
        raise ImportFromStringError(f"Couldn't find a dosei_config.py file in \"{os.getcwd()}\"")
    if app.command is None:
        raise ImportFromStringError('Command "run" not found.')
    os.system(app.command)


def dev():
    try:
        app: Dosei = import_from_string(dosei_config_init)
    except ImportFromStringError:
        raise ImportFromStringError(f"Couldn't find a dosei_config.py file in \"{os.getcwd()}\"")
    if app.dev is None:
        raise ImportFromStringError('Command "dev" not found.')
    os.system(app.dev)


def export():
    try:
        app: Dosei = import_from_string(dosei_config_init)
        return app.export()
    except ImportFromStringError:
        raise ImportFromStringError(f"Couldn't find a dosei_config.py file in \"{os.getcwd()}\"")
