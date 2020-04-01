import json
from flask import Response
from uuid import UUID
import datetime


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


# ->31.02.1337-15h
APPLICATION_DATE_FORMAT = "%d-%m-%Y-%Hh"


class Case:
    uuid: UUID
    level_of_trust: int
    created_at: datetime
    longitude: float
    latitude: float

    @staticmethod
    def serialize_from_json(json_case_dict: dict):
        case = Case()
        case.uuid = UUID(json_case_dict["uuid"])
        case.latitude = json_case_dict["latitude"]
        case.longitude = json_case_dict["longitude"]
        case.created_at = datetime.datetime.strptime(json_case_dict["createdAt"], APPLICATION_DATE_FORMAT)
        case.level_of_trust = json_case_dict["levelOfTrust"]
        return case

    def deserialize_to_json(self):
        return {
            "uuid": str(self.uuid),
            "levelOfTrust": self.level_of_trust,
            "createdAt": self.created_at.strftime(APPLICATION_DATE_FORMAT),
            "longitude": self.longitude,
            "latitude": self.latitude
        }
