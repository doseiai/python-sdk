import os
import sys

from dosei_sdk import Dosei
from dosei_sdk.importer import import_from_string, ImportFromStringError

dosei_init = "dosei:dosei"

# Add current dir to PYTHONPATH
sys.path.insert(0, "")


def run(func):
    if func:
        return Dosei.call_func(import_from_string(func))
    try:
        app: Dosei = import_from_string(dosei_init)
    except ImportFromStringError:
        raise ImportFromStringError(f"Couldn't find a dosei.py file in \"{os.getcwd()}\"")
    if app.command is None:
        raise ImportFromStringError('Command "run" not found.')
    os.system(app.run)


def export():
    try:
        app: Dosei = import_from_string(dosei_init)
        return app.export()
    except ImportFromStringError:
        raise ImportFromStringError(f"Couldn't find a dosei.py file in \"{os.getcwd()}\"")
