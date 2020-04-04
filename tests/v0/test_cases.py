from flask import url_for
from typing import List
from uuid import uuid4, UUID
from db.db import DBConnection
import json
from flask.testing import FlaskClient
from flask import Response
from datetime import datetime
from itertools import repeat
from random import randrange, uniform
import time
from datetime import datetime, timedelta
from models.case import Case
from models.contact import Contact
import os


def random_time_in_the_past() -> datetime:
    # FIXME: use a cryptographically secure RNG
    now: datetime = datetime.now()
    one_day_ago: datetime = now - timedelta(days=1)
    noise_minutes: int = randrange(start=0, stop=60 * 24 * 6, step=1)
    # anything between 1 and 7 days ago
    return one_day_ago - timedelta(minutes=noise_minutes)


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


def test_insert(client: FlaskClient):
    dbConn = DBConnection(os.environ.get("MONGO_URI"))
    # TODO: actually test that case is inserted
    prev_count: int = dbConn.count_cases()
    n: int = 10
    cases: list = generate_random_cases(n)
    res: Response = client.post(
        url_for("v0.cases.report"),
        data=json.dumps([case.__dict__ for case in cases], cls=CaseEncoder),
        content_type="application/json",
    )
    assert res.status_code == 201
    assert dbConn.count_cases() == (prev_count + n)


# copied from https://stackoverflow.com/a/48159596/9926795
class CaseEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)
