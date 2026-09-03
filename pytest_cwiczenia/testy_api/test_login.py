import requests
import pytest


@pytest.mark.login
def test_login(base_url, headers, login_data):
    # Act
    response = requests.post(f"{base_url}/login", headers=headers, json=login_data)

    # Assert
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["token_type"] == "bearer"
    # assert response_body.token_type == "bearer"
