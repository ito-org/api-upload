import json
from typing import List, Optional
from flask import Response
from datetime import datetime

# https://confluence.ito-app.org/display/IN/API+Documentation


class Contact:
    uuid: str
    lat: Optional[float]
    lon: Optional[float]
    trust_level: int
    upload_timestamp: datetime
    case_uuid: str

    def __init__(
        self,
        uuid: str,
        lat: Optional[float],
        lon: Optional[float],
        trust_level: int,
        upload_timestamp: datetime,
        case_uuid: str,
    ):
        self.uuid = uuid
        self.lat = lat
        self.lon = lon
        self.trust_level = trust_level
        self.upload_timestamp = upload_timestamp
        self.case_uuid = case_uuid

    def as_response(self, code: int) -> Response:
        return Response(
            json.dumps(self.__dict__), status=code, mimetype="application/json"
        )
