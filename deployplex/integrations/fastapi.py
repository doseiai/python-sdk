import os
from fastapi import HTTPException, Request, status, FastAPI


def cron_job_auth(request: Request):
    auth_header = request.headers.get("authorization")
    if auth_header != f"Bearer {os.getenv('DEPLOYPLEX_CRON_SECRET')}":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


def get_fastapi_app(app):
    while hasattr(app, "app"):
        app = app.app
    return app


class FastAPIMiddleware:
    _self = None
    _initialized = False

    def __new__(cls, app):
        if cls._self is None:
            cls._self = super(FastAPIMiddleware, cls).__new__(cls)
        return cls._self

    def __init__(self, app):
        if self._initialized:
            return
        self.app = get_fastapi_app(app)
        self.deprecated_endpoints = [route.path for route in self.app.routes if getattr(route, 'deprecated', False)]
        self._initialized = True

    async def __call__(self, scope, receive, send):
        if scope['type'] == 'http':
            path = scope.get("path")
            if path in self.deprecated_endpoints:
                print(f"Deprecated endpoint {path} accessed.")

        await self.app(scope, receive, send)


def init(app: FastAPI):
    # TODO: This doesn't work, is breaking tests somehow, implement somewhere in the future
    # for app in gc.get_objects():
    #     if isinstance(app, FastAPI):
    #         app.add_middleware(FastAPIMiddleware)
    #         return
    app.add_middleware(FastAPIMiddleware)
