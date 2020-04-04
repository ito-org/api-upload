from flask import Blueprint, request, Response, abort, current_app
from app.model import ApiError
from app.persistence.db import DBConnection


def construct_contacts_blueprint(dbConn: DBConnection):
    contacts = Blueprint("v0.contacts", __name__, url_prefix="/v0/contacts")

    @contacts.route("/report", methods=["POST"])
    def report() -> Response:
        abort(501)
        return Response(None, status=201)

    return contacts
