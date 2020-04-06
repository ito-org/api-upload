from flask import Flask
from pymongo import MongoClient
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, Iterator, List
from uuid import uuid4, UUID
from random import randrange, uniform
import time
from itertools import repeat
from app.model.case import Case
from app.model.contact import Contact


class DBConnection:
    db: Any

    def __init__(self, hostUri: str):
        client = MongoClient(hostUri)
        self.db = client.ito

    def insert_cases(self, cases: List[Any]) -> None:
        self.db.cases.insert_many(cases)

    def count_cases(self) -> int:
        return int(self.db.cases.count_documents({}))

    def insert_contacts(contacts: List[Contact]) -> None:
        mongo.db.contacts.insert_many(contacts)
        return

    def random_time_in_the_past(self) -> datetime:
        # FIXME: use a cryptographically secure RNG
        now: datetime = datetime.now()
        one_day_ago: datetime = now - timedelta(days=1)
        noise_minutes: int = randrange(start=0, stop=60 * 24 * 6, step=1)
        # anything between 1 and 7 days ago
        return one_day_ago - timedelta(minutes=noise_minutes)

    def insert_random_cases(self, n: int) -> None:
        for _ in repeat(None, n):
            self.db.cases.insert(
                {
                    "uuid": uuid4(),
                    "trust_level": 1,
                    "upload_timestamp": self.random_time_in_the_past(),
                    "lat": round(uniform(-90, 90), 1),
                    "lon": round(uniform(-180, 180), 1),
                }
            )

    def generate_random_cases(self, n: int) -> List[Any]:
        cases: List[Any] = []
        for _ in repeat(None, n):
            cases.append(
                {
                    "uuid": uuid4(),
                    "trust_level": 1,
                    "upload_timestamp": self.random_time_in_the_past(),
                    "lat": round(uniform(-90, 90), 1),
                    "lon": round(uniform(-180, 180), 1),
                }
            )
        return cases