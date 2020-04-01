from flask import Blueprint, request, Response, abort, current_app
from app.model import ApiError

cases = Blueprint("v0.cases", __name__, url_prefix="/v0/cases")


@cases.route("/v0/cases", methods=["POST"], strict_slashes=False)
def report_case():
    abort(501)
    return Response(None, status=201)


@cases.route("/v0/contacts", methods=["POST"], strict_slashes=False)
def report_contact():
    abort(501)
    return Response(None, status=201)