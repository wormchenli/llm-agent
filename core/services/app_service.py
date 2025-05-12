import uuid
from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session

from injector import inject

from core.models import AppEntity


@inject
@dataclass
class AppService:
    db: SQLAlchemy

    def create_app(self) -> AppEntity:
        app_entity = AppEntity(name="deepseek chat bot", icon="", description="Deepseek chat bot",
                               account_id=uuid.uuid4())

        with self.db.session.begin():
            self.db.session.add(app_entity)
        return app_entity

    def get_app(self, id: uuid.UUID) -> AppEntity:
        app_entity = self.db.session.query(AppEntity).get(id)
        return app_entity

    # def update_app(self, id: uuid.UUID, app: AppEntity) -> bool:
    # update
    def update_app(self, id: uuid.UUID, data: dict) -> bool:
        with self.db.session.begin():
            app_entity = self.db.session.get(AppEntity, id)
            if not app_entity:
                return False
            for key, value in data.items():
                if hasattr(app_entity, key):
                    setattr(app_entity, key, value)
        return True

    # delete
    def delete_app(self, id: uuid.UUID) -> bool:
        with self.db.session.begin():
            app_entity = self.db.session.get(AppEntity, id)
            if not app_entity:
                return False
            self.db.session.delete(app_entity)
        return True
