from flask import url_for
from uuid import uuid4, UUID
import json


def test_insert(client):
    # TODO: actually test that case is inserted
    res = client.post(url_for("v0.cases.report_case"))
    assert res.status_code == 501
