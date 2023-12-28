# Dosei Python SDK

`dosei` is the official Dosei SDK for Python

[![pypi version](https://img.shields.io/pypi/v/dosei.svg)](https://pypi.org/pypi/dosei/)
[![Downloads](https://static.pepy.tech/badge/dosei/week)](https://pypi.org/pypi/dosei/)
[![License: MIT](https://img.shields.io/badge/license-Apache--2.0-yellow)](https://www.apache.org/licenses/LICENSE-2.0)
[![Twitter](https://img.shields.io/twitter/url/https/x.com/dosei_ai.svg?style=social&label=Follow%20%40dosei_ai)](https://x.com/dosei_ai)
[![](https://dcbadge.vercel.app/api/server/BP5aUkhcAh?compact=true&style=flat)](https://discord.com/invite/BP5aUkhcAh)


## Getting Started

### Requirements
- [Python 3.11.2](https://www.python.org/downloads/)

### Install
You can install and configure `dosei` using this command:
```bash
pip install -U dosei
```

### Configure

```python
from fastapi import FastAPI
import dosei.integrations.fastapi as dosei_fastapi_integration

app = FastAPI()
dosei_fastapi_integration.init(app)
```
