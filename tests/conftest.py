import pytest
from clients.api_client import APIClient
from endpoints.user_endpoints import UserEndPoints


@pytest.fixture(scope="session")
def api_client():
    client = APIClient()
    # Login and store authentication token
    response = client.request("POST", "/"
                                      "/login",
                              json={
                                  "username": "admin",
                                  "password": "admin123"
                              }
                              )
    token = response.json()["token"]
    client.add_token(token)
    return client
@pytest.fixture(scope="function")
def user_service(api_client):
    return UserEndPoints(api_client)
