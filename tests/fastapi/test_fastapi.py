from dosei_sdk import Dosei
from dosei_sdk.importer import import_from_string


def test_fastapi():
    app: Dosei = import_from_string("tests.fastapi.dosei_config:dosei")
    assert app.name == "hello-world"
    assert app.port == 8080
    assert app.run == f"uvicorn helloworld.main:app --host 0.0.0.0 --port {app.port}"
