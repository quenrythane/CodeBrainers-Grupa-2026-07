import requests
import pytest


@pytest.mark.delete_employee
def test_delete_employee(base_url, auth_headers, employee_data):

    # Arrange - najpierw tworzymy pracownika, aby go usunąć
    create_response = requests.post(f"{base_url}/employees", headers=auth_headers, json=employee_data)
    created_employee = create_response.json()
    employee_id = created_employee["id"]

    # Act
    response = requests.delete(f"{base_url}/employees/{employee_id}", headers=auth_headers)

    # Assert
    assert response.status_code == 200

    # Weryfikacja czy pracownik rzeczywiście został usunięty z listy
    get_all_response = requests.get(f"{base_url}/employees", headers=headers)
    assert get_all_response.status_code == 200
    employees_ids = [emp["id"] for emp in get_all_response.json()]
    assert employee_id not in employees_ids
