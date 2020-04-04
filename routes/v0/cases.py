from flask import Blueprint, request, Response, abort, current_app, jsonify
from models.api import ApiError
from models.case import Case
from db.db import DBConnection
from typing import Any, Optional, List, Union, Generator
from uuid import UUID
import json


def construct_cases_blueprint(dbConn: DBConnection):
    cases = Blueprint("v0.cases", __name__, url_prefix="/v0/cases")

    @cases.route("/", methods=["GET"], strict_slashes=False)
    def index() -> Response:
        lat: Union[Optional[float], int] = request.args.get("lat", type=float)
        lon: Union[Optional[float], int] = request.args.get("lon", type=float)
        uuid: Optional[UUID] = request.args.get("uuid", type=UUID)

        if uuid is None:
            return ApiError(400, "No valid UUID for the requested query").as_response()

        try:
            if lat is not None:
                lat = round(lat)
            if lon is not None:
                lon = round(lon)
        except ValueError:
            abort(400)

        cases = dbConn.get_cases(uuid, lat=lat, lon=lon)

        def generate() -> Generator[str, None, None]:
            for case in cases:
                case_uuid = str(case["uuid"])
                yield case_uuid + ","

        return Response(generate(), mimetype="application/octet-stream")

    @cases.route("/report", methods=["POST"])
    def report() -> Response:
        # TODO: check that user's infection has been verified
        if not (current_app.config["DEBUG"] or current_app.config["TESTING"]):
            return ApiError(
                501, "only available in dev and testing for now"
            ).as_response()
        cases: Optional[List[Any]] = request.get_json()
        if cases is None:
            return ApiError(
                400, "please use the application/json content type",
            ).as_response()
        dbConn.insert_cases(cases)
        return Response(None, status=201)

    return cases