import json
from uuid import UUID
from typing import List, Optional
from flask import Response
from datetime import datetime

# https://confluence.ito-app.org/display/IN/API+Documentation


class Case:
    uuid: UUID
    lat: Optional[float]
    lon: Optional[float]
    trust_level: int
    upload_timestamp: datetime

    def __init__(
        self,
        uuid: UUID,
        lat: Optional[float],
        lon: Optional[float],
        trust_level: int,
        upload_timestamp: datetime,
    ):
        self.uuid = uuid
        self.lat = lat
        self.lon = lon
        self.trust_level = trust_level
        self.upload_timestamp = upload_timestamp

    def toJSON(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__)

    def as_response(self, code: int) -> Response:
        return Response(self.toJSON(), status=code, mimetype="application/json")
