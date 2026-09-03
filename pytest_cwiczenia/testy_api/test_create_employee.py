import requests
import pytest


@pytest.mark.create_employee
def test_create_employee(base_url, headers, employee_data, auth_token):
    # Act
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(f"{base_url}/employees", headers=headers, json=employee_data)

    # Assert
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["name"] == "Cezary"
    assert response_body["salary"] == 4000
    assert response_body["age"] == 30
    assert response_body["position"] == "Junior QA"
    assert response_body["on_leave"] == True
