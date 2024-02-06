import os
from dosei import Dosei

port = os.getenv('PORT', 8080)
dosei = Dosei(
    name="hello-world",
    command=f"uvicorn helloworld.main:app --host 0.0.0.0 --port {port}",
    dev=f"uvicorn tests.fastapi.helloworld.main:app --port {port} --reload",
    port=port
)
