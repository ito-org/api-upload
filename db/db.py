from flask import Flask
from pymongo import MongoClient
from typing import Optional, Dict, Any, Iterator, List
from uuid import uuid4, UUID
from datetime import datetime, timedelta
import time
from random import randrange
from models.case import Case
from models.contact import Contact


class DBConnection:
    db: Any

    def __init__(self, hostUri: str):
        client = MongoClient(hostUri)
        self.db = client.ito

    def insert_cases(self, cases: List[Any]) -> None:
        self.db.cases.insert_many(cases)

    def count_cases(self) -> int:
        return int(self.db.cases.count_documents({}))

    def insert_contacts(self, contacts: List[Contact]) -> None:
        self.db.contacts.insert_many(contacts)
        return

    def get_cases(
        self, uuid: UUID, lat: Optional[int] = None, lon: Optional[int] = None
    ) -> Iterator[Case]:
        # TODO: prevent timing attacks that could reveal if a UUID is present or not
        conditions: Dict[str, Any] = {}
        if lat is not None:
            conditions["lat"] = lat
        if lon is not None:
            conditions["lon"] = lon
        conditions["uuid"] = str(uuid)

        # if last_case is None:
        #    conditions["upload_timestamp"] = {"$gte": self.random_time_in_the_past()}
        # else:
        #    conditions["upload_timestamp"] = {"$gte": last_case["upload_timestamp"]}
        return (case for case in self.db.cases.find(conditions))

    def random_time_in_the_past(self) -> datetime:
        # FIXME: use a cryptographically secure RNG
        now: datetime = datetime.now()
        one_day_ago: datetime = now - timedelta(days=1)
        noise_minutes: int = randrange(start=0, stop=60 * 24 * 6, step=1)
        # anything between 1 and 7 days ago
        return one_day_ago - timedelta(minutes=noise_minutes)
