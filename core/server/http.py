from flask import Flask
from core.routers import Router
from configs import Config
from flask_sqlalchemy import SQLAlchemy


# customize a Flask class
class HttpServer(Flask):
    def __init__(self, *args, config: Config, db: SQLAlchemy, router: Router, **kwargs):
        super().__init__(*args, **kwargs)

        # load config
        self.config.from_object(config)

        # init router
        router.register_router(self)

        # init db
        db.init_app(self)
        with self.app_context():
            db.create_all()
