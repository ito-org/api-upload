from flask import Blueprint, request, Response, abort, current_app
from model import ApiError
from model.contact import Contact
from persistence.db import DBConnection
from typing import Any, Optional, List


def construct_contacts_blueprint(dbConn: DBConnection):
    contacts = Blueprint("v0.contacts", __name__, url_prefix="/v0/contacts")

    @contacts.route("/report", methods=["POST"])
    def report() -> Response:
        abort(501)
        if not (current_app.config["DEBUG"] or current_app.config["TESTING"]):
            return ApiError(
                501, "only available in dev and testing for now"
            ).as_response()
        contacts: Optional[List[Contact]] = request.get_json()
        if contacts is None:
            return ApiError(
                400, "please use the application/json content type"
            ).as_response()
        dbConn.insert_contacts(contacts)
        return Response(None, status=201)

    return contacts
