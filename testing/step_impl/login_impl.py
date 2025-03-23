import requests
from getgauge.python import step, data_store, before_spec

BASE_URL = "http://localhost:3000"


@before_spec()
def create_correct_user():
    requests.post(
        f"{BASE_URL}/auth/register",
        json={
            "name": "name",
            "surname": "surname",
            "email": "correct_user@example.com",
            "password": "correct_password"
        }
    )
    print("Registered new user")


@step("Send a POST request to <url> with email <email> and password <password>")
def send_post_request(url: str, email: str, password: str) -> None:
    full_url = f"{BASE_URL}{url}"
    response = requests.post(full_url, json={"email": email, "password": password})
    data_store.scenario['response'] = response
    print(f"Request was sent successfully to url {url}")


@step("Verify response status is <status_code>")
def verify_response_status(status_code: str) -> None:
    response_code = data_store.scenario['response'].status_code
    assert response_code == int(status_code)
    print(f"Response status {status_code} was verified")


@step("Verify response contains <key> with data <value>")
def verify_response_contains(key: str, value: str) -> None:
    response_data = data_store.scenario['response'].json()
    assert response_data[key] == value
    print(f"Response contains {key} with data {value}")
