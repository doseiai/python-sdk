from dosei import Dosei

dosei = Dosei(
    name="hello-world",
    command="uvicorn helloworld.main:app --host 0.0.0.0",
    dev="uvicorn tests.fastapi.helloworld.main:app --reload",
    port=8080
)
