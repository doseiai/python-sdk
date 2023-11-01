# DeployPlex Python SDK

`deployplex` is the official DeployPlex SDK for Python

[![pypi version](https://img.shields.io/pypi/v/deployplex.svg)](https://pypi.org/pypi/deployplex/)
[![Downloads](https://static.pepy.tech/badge/deployplex/week)](https://pypi.org/pypi/deployplex/)
[![License: MIT](https://img.shields.io/badge/license-Apache--2.0-yellow)](https://www.apache.org/licenses/LICENSE-2.0)
[![Twitter](https://img.shields.io/twitter/url/https/x.com/deployplex.svg?style=social&label=Follow%20%40deployplex)](https://x.com/deployplex)
[![](https://dcbadge.vercel.app/api/server/BP5aUkhcAh?compact=true&style=flat)](https://discord.com/invite/BP5aUkhcAh)


## Getting Started

### Requirements
- [Python 3.11.2](https://www.python.org/downloads/)

### Install
You can install and configure `deployplex` using this command:
```bash
pip install -U deployplex
```

### Configure
```python
from fastapi import FastAPI
import deployplex.integrations.fastapi as deployplex_fastapi_integration

app = FastAPI()
deployplex_fastapi_integration.init(app)
```

### Auth for DeployPlex CronJob endpoints
```python
from fastapi import FastAPI, Depends, Response
from deployplex.integrations.fastapi import cron_job_auth

app = FastAPI()

@app.post("/job")
def job(auth: None = Depends(cron_job_auth)) -> Response:
    return Response()
```
