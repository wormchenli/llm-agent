import dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from injector import Injector

from core.server import HttpServer
from core.routers import Router
from core.extensions.database_extension import DBModule
from configs import Config

dotenv.load_dotenv()

injector = Injector([DBModule])
app_config = Config()

app = HttpServer(
    "LLM Server",
    config=app_config,
    db=injector.get(SQLAlchemy),
    migrate=injector.get(Migrate),
    router=injector.get(Router)
)

if __name__ == "__main__":
    app.run(debug=True)
