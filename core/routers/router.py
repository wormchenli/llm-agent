from flask import Flask, Blueprint
from injector import inject
from dataclasses import dataclass

from core.controllers import AppController


@inject
@dataclass
class Router:
    app_controller: AppController

    def register_router(self, app: Flask):
        bp = Blueprint("base", __name__, url_prefix="/")

        bp.add_url_rule("/ping", methods=["GET"], view_func=self.app_controller.ping)
        bp.add_url_rule("/completion", methods=["POST"], view_func=self.app_controller.completion)
        bp.add_url_rule("/app", methods=["POST"], view_func=self.app_controller.create_app)
        bp.add_url_rule("/app/<uuid:id>", methods=["GET"], view_func=self.app_controller.get_app)
        bp.add_url_rule("/app/<uuid:id>", methods=["PUT"], view_func=self.app_controller.update_app)
        bp.add_url_rule("/app/<uuid:id>", methods=["DELETE"], view_func=self.app_controller.delete_app)

        app.register_blueprint(bp)
