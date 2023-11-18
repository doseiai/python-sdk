from fastapi import FastAPI, Response
from fastapi.testclient import TestClient
import dosei.integrations.fastapi as dosei_fastapi_integration

app = FastAPI()
dosei_fastapi_integration.init(app)

client = TestClient(app)


@app.get("/deprecated", deprecated=True)
def deprecated() -> Response:
    return Response()


@app.get("/not-deprecated")
def not_deprecated() -> Response:
    return Response()


def test_deprecated():
    response = client.get("/deprecated")
    assert response.status_code == 200

    instance = dosei_fastapi_integration.FastAPIMiddleware(app)
    assert "/deprecated" in instance.deprecated_endpoints


def test_not_deprecated():
    response = client.get("/not-deprecated")
    assert response.status_code == 200

    instance = dosei_fastapi_integration.FastAPIMiddleware(app)
    assert "/not-deprecated" not in instance.deprecated_endpoints
