from flask import Flask
import os
from flask import Flask
from db.db import DBConnection

from routes.v0.cases import construct_cases_blueprint
from routes.v0.contacts import construct_contacts_blueprint


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


app: Flask = create_app()
