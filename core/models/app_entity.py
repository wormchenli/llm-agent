import uuid
from datetime import datetime

from core.models.dbModule import db
from sqlalchemy import (
    Column,
    UUID,
    String,
    Text,
    DateTime,
    PrimaryKeyConstraint,
    Index
)


class AppEntity(db.Model):
    __tablename__ = "llm-app"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="app_id_pk"),
        Index("app_account_id_idx", "account_id"),
    )

    id = Column(UUID, default=uuid.uuid4, nullable=False, primary_key=True)
    account_id = Column(UUID, nullable=False)
    name = Column(String(255), default="", nullable=False)
    icon = Column(String(255), default="", nullable=False)
    description = Column(Text, default="", nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False, onupdate=datetime.now)
    created_at = Column(DateTime, default=datetime.now, nullable=False, onupdate=datetime.now)
