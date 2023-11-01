import os

from fastapi import FastAPI, Depends, Response, status
from fastapi.testclient import TestClient
from deployplex.integrations.fastapi import cron_job_auth

os.environ["DEPLOYPLEX_CRON_SECRET"] = "deployplex_cron_secret_test_value"

app = FastAPI()


@app.post("/job")
def job(auth: None = Depends(cron_job_auth)) -> Response:
    return Response()


client = TestClient(app)


def test_job():
    response = client.post("/job", headers={"Authorization": f'Bearer {os.environ["DEPLOYPLEX_CRON_SECRET"]}'})
    assert response.status_code == status.HTTP_200_OK


def test_unauthorized_job():
    response = client.post("/job")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
