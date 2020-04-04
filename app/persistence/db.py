from flask import Flask
from flask_pymongo import PyMongo  # type: ignore
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, Iterator, List
from uuid import uuid4, UUID
from random import randrange, uniform
import time
from itertools import repeat
from app.model.case import Case
from app.model.contact import Contact

mongo = PyMongo()


def insert_cases(cases: List[Case]) -> None:
    mongo.db.cases.insert_many(cases)


def count_cases() -> int:
    return int(mongo.db.cases.count_documents({}))


def insert_contacts(contacts: List[Contact]) -> None:
    mongo.db.contacts.insert_many(contacts)
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
            Case(
                uuid4(),
                round(uniform(-90, 90), 1),
                round(uniform(-180, 180), 1),
                1,
                random_time_in_the_past(),
            )
        )


def generate_random_cases(n: int) -> List[Case]:
    cases: List[Case] = []
    for _ in repeat(None, n):
        cases.append(
            Case(
                uuid4(),
                round(uniform(-90, 90), 1),
                round(uniform(-180, 180), 1),
                1,
                random_time_in_the_past(),
            )
        )
    return cases
