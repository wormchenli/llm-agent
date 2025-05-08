import dotenv
from flask_sqlalchemy import SQLAlchemy

from injector import Injector

from core.server import HttpServer
from core.routers import Router
from core.models.dbModule import DBModule
from configs import Config

dotenv.load_dotenv()

injector = Injector([DBModule])
app_config = Config()

app = HttpServer("LLM Server", config=app_config, db=injector.get(SQLAlchemy), router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)
