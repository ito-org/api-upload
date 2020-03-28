from flask import Flask, escape, request, jsonify, Response, abort
from datetime import datetime
from db import mongo, insert_case, insert_contact
import dateutil.parser as dateparser
from uuid import UUID
from typing import Union, Optional
import os

app = Flask(__name__, instance_relative_config=True)
env = os.environ.get("FLASK_ENV", "production")
if env == "production":
    app.config.from_object("config.ProductionConfig")
elif env == "development":
    app.config.from_object("config.DevelopmentConfig")
elif env == "testing":
    app.config.from_object("config.TestingConfig")


app.config["APPLICATION_ROOT"] = "/"

mongo.init_app(app)


@app.route("/v1/cases/report", methods=["POST"])
def report_case():
    abort(501)
    return Response(None, status=201)


@app.route("/v1/contacts/report", methods=["POST"])
def report_contact():
    abort(501)
    return Response(None, status=201)
