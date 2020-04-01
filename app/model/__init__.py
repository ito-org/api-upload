import json
from flask import Response


class ApiError:
    code: int
    message: str

    def __init__(self, code: int = None, message: str = None):
        if code is None:
            self.code = 500
        else:
            self.code = code

        if message is None:
            self.message = "Some unexpected condition occurred"
        else:
            self.message = message

    def as_response(self) -> Response:
        return Response(
            json.dumps(self.__dict__), status=self.code, mimetype="application/json"
        )
