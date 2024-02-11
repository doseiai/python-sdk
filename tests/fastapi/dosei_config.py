import os
from dosei_sdk import Dosei

port = os.getenv('PORT', 8080)
dosei = Dosei(
    name="hello-world",
    run=f"uvicorn helloworld.main:app --host 0.0.0.0 --port {port}",
    port=port
)
