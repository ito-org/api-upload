from flask import Flask
from flask_pymongo import PyMongo  # type: ignore
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, Iterator, List
from uuid import uuid4, UUID
from random import randrange, uniform
import time
from itertools import repeat

mongo = PyMongo()


def insert_cases(cases: List[Any]) -> None:
    mongo.db.cases.insert_many(cases)


def count_cases() -> int:
    return int(mongo.db.cases.count_documents({}))


def insert_contact() -> None:
    return


def random_time_in_the_past() -> datetime:
    # FIXME: use a cryptographically secure RNG
    now: datetime = datetime.now()
    one_day_ago: datetime = now - timedelta(days=1)
    noise_minutes: int = randrange(start=0, stop=60 * 24 * 6, step=1)
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


def generate_random_cases(n: int) -> List[Any]:
    cases: List[Any] = []
    for _ in repeat(None, n):
        cases.append(
            {
                "uuid": uuid4(),
                "trust_level": 1,
                "upload_timestamp": random_time_in_the_past(),
                "lat": round(uniform(-90, 90), 1),
                "lon": round(uniform(-180, 180), 1),
            }
        )
    return cases
