from enum import Enum


class HttpStatusCode(Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    NOT_FOUND = "not_found"
    UNAUTHORIZED = "unauthorized"
    FORBIDDEN = "forbidden"

    @property
    def get_code(self):
        if self == HttpStatusCode.SUCCESS:
            return 200
        elif self == HttpStatusCode.FAILURE:
            return 500
        elif self == HttpStatusCode.NOT_FOUND:
            return 404
        elif self == HttpStatusCode.UNAUTHORIZED:
            return 401
        elif self == HttpStatusCode.FORBIDDEN:
            return 403
        else:
            return 400
