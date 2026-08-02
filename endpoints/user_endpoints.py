from clients.api_client import APIClient


class UserEndPoints:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def create_user(self, payload: dict):
        self.api_client.request("POST", "/users", json=payload)

    def get_user(self, user_id: int):
        self.api_client.request("GET", "/users/{user_id}".format(user_id=user_id))
