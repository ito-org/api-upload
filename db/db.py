from flask import Flask
from pymongo import MongoClient  # type: ignore
from typing import Optional, Dict, Any, Iterator, List
from uuid import uuid4, UUID
from datetime import datetime
import time
from random import randrange
from models.case import Case
from models.contact import Contact


class DBConnection:
    db: Any

    def __init__(self, hostUri: Optional[str]):
        if hostUri is None:
            hostUri = "mongodb://localhost:27017"
        client = MongoClient(hostUri)
        self.db = client.ito

    def insert_reportsig(self, reportsig: str, timestamp: datetime) -> None:
        self.db.reportsigs.insert_one({"reportsig": reportsig, "timestamp": timestamp})

    def get_reportsigs(self) -> List[str]:
        return list(self.db.reportsigs.find({}, {"_id": False}))
