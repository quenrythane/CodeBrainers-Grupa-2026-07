import requests


# AAA - Arrange, Act, Assert

# Arrange
BASE_URL = "http://127.0.0.1:8000/api"
LOGIN_ENDPOINT = "login"
url = f"{BASE_URL}/{LOGIN_ENDPOINT}"

request_headers = {"accept": "application/json"}

request_body = {
    "username": "admin",
    "password": "admin"
}

# Act
response = requests.post(url, headers=request_headers, json=request_body)

# Assert
response_status_code = response.status_code
response_body = response.json()

print(response_status_code)
print(response_body)