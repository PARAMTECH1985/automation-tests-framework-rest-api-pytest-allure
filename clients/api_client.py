import requests
import allure
from config.config import Config


class APIClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = {"Content-Type": "application/json"}

    def add_token(self, token: str):
        self.headers["Authorization"] = f"Bearer {token}"

    @allure.step("Sending {method} request to {endpoint}")
    def request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        kwargs["headers"] = {**self.headers, **kwargs.get("headers", {})}
        kwargs["timeout"] = Config.TIMEOUT
        if 'json' in kwargs:
            allure.attach(kwargs["json"], name="Request Body", attachment_type=allure.attachment_type.JSON)
        response = requests.request(method, url, **kwargs)
        allure.attach(str(response.status_code), name="Response Status Code",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name="Response Text", attachment_type=allure.attachment_type.JSON)
        return response
