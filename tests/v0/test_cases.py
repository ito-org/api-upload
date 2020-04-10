import json
from datetime import datetime
from flask import url_for, Response
from flask.testing import FlaskClient


def test_report_post(client: FlaskClient):
    data = {
        "reportsig": "teststr",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    res: Response = client.post(
        url_for(".report"), data=json.dumps(data), content_type="application/json"
    )
    assert res.status_code == 200
