from flask import Flask
from flask_pymongo import PyMongo  # type: ignore
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, Iterator
from uuid import uuid4, UUID
from random import randrange, uniform
import time
from itertools import repeat

db = mongo = PyMongo()


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


def random_time_in_the_past() -> datetime:
    # FIXME: use a cryptographically secure RNG
    now = datetime.now()
    one_day_ago = now - timedelta(days=1)
    noise_minutes = randrange(start=0, stop=60 * 24 * 6, step=1)
    # anything between 1 and 7 days ago
    return one_day_ago - timedelta(minutes=noise_minutes)


def insert_random_cases(n: int) -> None:
    for _ in repeat(None, n):
        mongo.db.cases.insert(
            {
                "uuid": uuid4(),
                "trust_level": 1,
                "upload_timestamp": random_time_in_the_past(),
                "lat": round(uniform(-90, 90), 1),
                "lon": round(uniform(-180, 180), 1),
            }
        )
