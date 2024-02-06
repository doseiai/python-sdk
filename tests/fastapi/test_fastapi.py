from dosei import Dosei
from dosei.importer import import_from_string


def test_fastapi():
    app: Dosei = import_from_string("tests.fastapi.dosei:dosei")
    assert app.name == "hello-world"
    assert app.port == 8080
    assert app.command == "uvicorn helloworld.main:app --host 0.0.0.0"
