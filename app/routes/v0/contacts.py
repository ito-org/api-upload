from flask import Blueprint, request, Response, abort, current_app
from app.model import ApiError


contacts = Blueprint("v0.contacts", __name__, url_prefix="/v0/contacts")


@contacts.route("/report", methods=["POST"])
def report() -> Response:
    abort(501)
    return Response(None, status=201)
