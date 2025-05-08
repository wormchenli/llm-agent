import os


class Config:
    def __init__(self):
        # model configs
        self.model_name = os.environ.get("MODEL_NAME")
        self.WTF_CSRF_ENABLED = os.environ.get("WTF_CSRF_ENABLED", "True").lower() != "false"

        # db configs
        self.SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI")
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size": int(os.environ.get("DB_POOL_SIZE")),
            "pool_recycle": int(os.environ.get("DB_POOL_RECYCLE"))
        }
        self.SQLALCHEMY_ECHO = os.environ.get("DB_ECHO", "True").lower() != "false"
