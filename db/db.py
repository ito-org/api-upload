from flask import Flask
from pymongo import MongoClient
from typing import Optional, Dict, Any, Iterator, List
from uuid import uuid4, UUID
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
