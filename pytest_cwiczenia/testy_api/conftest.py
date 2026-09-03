import pytest
import requests

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


@pytest.fixture(autouse=True)
def employee_data():
    request_body = {
        "name": "Cezary",
        "salary": 4000,
        "age": 30,
        "position": "Junior QA",
        "on_leave": True
    }
    return request_body

@pytest.fixture(autouse=True)
def auth_token(base_url, headers, login_data):
    response = requests.post(f"{base_url}/login", headers=headers, json=login_data)
    response_body = response.json()
    return response_body["access_token"]





