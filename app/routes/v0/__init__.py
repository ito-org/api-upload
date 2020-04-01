from flask import Blueprint, request, Response, abort, current_app
from uuid import UUID
from typing import Union, Optional
from app.persistence.db import insert_case
from app.model import ApiError

cases = Blueprint("v0.cases", __name__, url_prefix="/v0/cases")
contacts = Blueprint("v0.contacts", __name__, url_prefix="/v0/contacts")


@cases.route("/report", methods=["POST"])
def report_case():
    abort(501)
    return Response(None, status=201)


@contacts.route("/report", methods=["POST"])
def report_contact():
    abort(501)
    return Response(None, status=201)
