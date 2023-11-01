import os
from fastapi import HTTPException, Request, status


def cron_job_auth(request: Request):
    auth_header = request.headers.get("authorization")
    if auth_header != f"Bearer {os.getenv('DEPLOYPLEX_CRON_SECRET')}":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
