from core.server import HttpServer
from injector import Injector
from core.routers import Router

injector = Injector()

app = HttpServer("LLM Server", router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)
