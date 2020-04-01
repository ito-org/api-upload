from flask_pymongo import PyMongo  # type: ignore
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, Iterator
from uuid import uuid4, UUID
from random import randrange, uniform
import time
from itertools import repeat
from app.model import Case

db = mongo = PyMongo()


def insert_cases(cases):
    puttable_cases = map(Case.deserialize_to_json, cases)
    return None
