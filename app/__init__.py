import os
from flask import Flask
from app.persistence.db import DBConnection

from .routes.v0 import construct_cases_blueprint
from .routes.v0 import construct_contacts_blueprint


def create_app() -> Flask:
    app = Flask(__name__)

    env = os.environ.get("FLASK_ENV", "production")
    if env == "production":
        app.config.from_object("config.ProductionConfig")
    elif env == "development":
        app.config.from_object("config.DevelopmentConfig")
    elif env == "testing":
        app.config.from_object("config.TestingConfig")
        mongo_uri = os.environ.get("MONGO_URI")
        if mongo_uri is not None:
            app.config.update({"MONGO_URI": mongo_uri})

    dbConn = DBConnection(os.environ.get("MONGO_URI"))

    app.register_blueprint(construct_cases_blueprint(dbConn))
    app.register_blueprint(construct_contacts_blueprint(dbConn))

    return app
