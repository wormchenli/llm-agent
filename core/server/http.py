from flask import Flask
from core.routers import Router


class HttpServer(Flask):
    def __init__(self, *args, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        router.register_router(self)
