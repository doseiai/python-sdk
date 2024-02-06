from dosei import Dosei

dosei = Dosei(
    name="hello-world",
    command="uvicorn helloworld.main:app --host 0.0.0.0",
    port=8080
)
