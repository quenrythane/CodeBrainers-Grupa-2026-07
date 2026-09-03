import pytest

@pytest.fixture(autouse=True)
def base_url():
    BASE_URL = "http://127.0.0.1:8000/api"
    return BASE_URL

@pytest.fixture(autouse=True)
def headers():
    request_headers = {"accept": "application/json"}
    return request_headers

@pytest.fixture(autouse=True)
def login_data():
    request_body = {
        "username": "admin",
        "password": "admin"
    }
    return request_body



