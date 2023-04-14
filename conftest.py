from app import app


import pytest


@pytest.fixture
def create_client():
    with app.test_client() as client:
        return client