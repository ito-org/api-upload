from flask import Flask
import pytest  # type: ignore
from app import create_app


@pytest.fixture  # type: ignore
def app() -> Flask:
    return create_app()
