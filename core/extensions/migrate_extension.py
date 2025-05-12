from flask_migrate import Migrate
from injector import Module, Binder

migrate = Migrate()


class DBModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(Migrate, to=migrate)
