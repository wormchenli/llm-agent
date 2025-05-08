from .http_status_code import HttpStatusCode

from flask import jsonify


class ResponseBody:
    def __init__(self, status: HttpStatusCode, data=None, message=None):
        if not isinstance(status, HttpStatusCode):
            raise TypeError("status must be an HttpStatusCode enum value")

        self.status = status
        self.data = {} if data is None else data
        self.message = message if message is not None else ""
        self.code = status.get_code

    def to_response(self):
        response = {
            "status": self.status.name.lower(),
            "message": self.message,
            "code": self.code,
            "data": self.data
        }

        return jsonify(response), self.code

# ResponseBody(HttpCode.SUCCESS, data={"user": user}).to_response()
