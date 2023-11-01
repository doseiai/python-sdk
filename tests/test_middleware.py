from fastapi import FastAPI, Response
from fastapi.testclient import TestClient
import deployplex.integrations.fastapi as deployplex_fastapi_integration

app = FastAPI()
deployplex_fastapi_integration.init(app)

client = TestClient(app)


@app.get("/deprecated", deprecated=True)
def deprecated() -> Response:
    return Response()


@app.get("/not-deprecated")
def not_deprecated() -> Response:
    return Response()


# TODO: Test somehow
