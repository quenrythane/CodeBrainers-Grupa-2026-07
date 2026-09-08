import requests
import pytest


@pytest.mark.create_employee
def test_create_employee(base_url, auth_headers, employee_data):
    # Act
    response = requests.post(f"{base_url}/employees", headers=auth_headers, json=employee_data)

    # Assert
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["name"] == "Cezary"
    assert response_body["salary"] == 3000
    assert response_body["age"] == 30
    assert response_body["position"] == "Junior QA"
    assert response_body["on_leave"] == True
