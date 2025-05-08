import uuid
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from injector import inject

from core.models import AppEntity


@inject
@dataclass
class AppService:
    db: SQLAlchemy

    def create_app(self) -> AppEntity:
        app_entity = AppEntity(name="deepseek chat bot", icon="", description="Deepseek chat bot",
                               account_id=uuid.uuid4())

        self.db.session.add(app_entity)
        self.db.session.commit()
        return app_entity

    def get_app(self, id: uuid.UUID) -> AppEntity:
        app = self.db.session.query(AppEntity).get(id)
        return app

    def update_app(self, id: uuid.UUID, app: AppEntity) -> bool:


