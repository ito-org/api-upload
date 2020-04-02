from flask import Blueprint, request, Response, abort, current_app
from app.model import ApiError
from app.persistence.db import insert_cases
from typing import Any, Optional, List

cases = Blueprint("v0.cases", __name__, url_prefix="/v0/cases")


@cases.route("/report", methods=["POST"])
def report() -> Response:
    # TODO: check that user's infection has been verified
    if not (current_app.config["DEBUG"] or current_app.config["TESTING"]):
        return ApiError(501, "only available in dev and testing for now").as_response()
    cases: Optional[List[Any]] = request.get_json()
    if cases is None:
        return ApiError(
            400, "please use the application/json content type",
        ).as_response()
    insert_cases(cases)
    return Response(None, status=201)
