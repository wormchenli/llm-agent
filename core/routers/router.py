from flask import Flask, Blueprint
from injector import inject
from dataclasses import dataclass

from core.controllers import AppController


@inject
@dataclass
class Router:
    app_controller: AppController

    def register_router(self, app: Flask):
        bp = Blueprint("llm", __name__, url_prefix="/llm")

        bp.add_url_rule("/ping", methods=["GET"], view_func=self.app_controller.ping)

        app.register_blueprint(bp)
