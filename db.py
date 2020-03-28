from flask import Flask
from flask_pymongo import PyMongo  # type: ignore
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, Iterator
from uuid import uuid4, UUID
from random import randrange, uniform
import time
from itertools import repeat

mongo = PyMongo()


def insert_case(uuid: UUID, lat: int = None, lon: int = None) -> None:
    mongo.db.cases.insert(
        {
            "uuid": uuid,
            "trust_level": 0,
            "upload_timestamp": datetime.now(),
            "lat": round(uniform(-90, 90), 1),
            "lon": round(uniform(-180, 180), 1),
        }
    )


def insert_contact() -> None:
    return
