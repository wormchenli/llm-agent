from flask_sqlalchemy import SQLAlchemy
from injector import Binder
from injector import Module

db = SQLAlchemy()


# dependency injection module for SQLAlchemy
class DBModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
