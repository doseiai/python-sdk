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

    def __init__(self, app):
        self.app = get_fastapi_app(app)
        self.deprecated_endpoints = [route.path for route in self.app.routes if getattr(route, 'deprecated', False)]

    async def __call__(self, scope, receive, send):
        if scope['type'] == 'http':
            path = scope.get("path")
            if path in self.deprecated_endpoints:
                print(f"Deprecated endpoint {path} accessed.")

        await self.app(scope, receive, send)


def init(app: FastAPI):
    # TODO: This doesn't work, is breaking tests somehow, not work investing now
    # for app in gc.get_objects():
    #     if isinstance(app, FastAPI):
    #         app.add_middleware(FastAPIMiddleware)
    #         return
    app.add_middleware(FastAPIMiddleware)
