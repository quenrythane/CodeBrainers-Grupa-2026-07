import requests
import pytest


@pytest.mark.delete_employee
def test_delete_employee(base_url, auth_headers, employee_data):

    # Arrange - najpierw tworzymy pracownika, którego będziemy mogli usunąć
    create_response = requests.post(f"{base_url}/employees", headers=auth_headers, json=employee_data)
    created_employee = create_response.json()
    employee_id = created_employee["id"]  # po stworzeniu pracownika pobieramy jego id żeby móc usunąć pracownika o tym konkretnym id

    # Act
    response = requests.delete(f"{base_url}/employees/{employee_id}", headers=auth_headers)  # usuwamy pracownika

    # Assert
    assert response.status_code == 200

    # Weryfikacja czy pracownik rzeczywiście został usunięty z listy
    get_all_response = requests.get(f"{base_url}/employees", headers=auth_headers)
    assert get_all_response.status_code == 200
    employees_ids = [emp["id"] for emp in get_all_response.json()]  # lista wszystkich id pracowników
    assert employee_id not in employees_ids  # sprawdzamy czy id usuniętego pracownika nie ma na liście pracowników
