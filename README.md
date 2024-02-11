# Dosei Python SDK

`dosei-sdk` is the official Dosei SDK for Python

[![pypi version](https://img.shields.io/pypi/v/dosei-sdk.svg)](https://pypi.org/pypi/dosei-sdk/)
[![](https://img.shields.io/discord/1144175748559683615?logo=discord&logoColor=7289DA&label=Discord)](https://discord.com/invite/BP5aUkhcAh)
[![X (formerly Twitter)](https://img.shields.io/twitter/follow/dosei_ai?style=flat&logo=x)](https://x.com/dosei_ai)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-white)](https://www.apache.org/licenses/LICENSE-2.0)


## Getting Started

### Requirements
- [Python 3.11.2](https://www.python.org/downloads/)

### Install
You can install and configure `dosei-sdk` using this command:

```bash
pip install -U dosei-sdk
```

### Configure

```python
from dosei_sdk import Dosei

dosei = Dosei()

@dosei.cron_job("* * * * *")
def cron_job():
    print("hello world!")
```
