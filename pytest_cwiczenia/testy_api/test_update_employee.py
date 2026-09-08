import requests
import pytest


@pytest.mark.update_employee
def test_update_employee(base_url, auth_headers, employee_update_data):
    # Act
    employee_id = 1
    response = requests.put(f"{base_url}/employees/{employee_id}", headers=auth_headers, json=employee_update_data)

    # Assert
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["name"] == "Damian"
    assert response_body["salary"] == 4000
    assert response_body["age"] == 40
    assert response_body["position"] == "Senior QA"
    assert response_body["on_leave"] == False
