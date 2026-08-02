import allure
import pytest

@allure.epic("User Management System")
@allure.feature("User CRUD Operations")
class TestUserManagement:
    @allure.story("Create User Account")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_create_user_account(self,user_service):
        payload =  {"name": "Alex", "job": "Engineer"}
        response = user_service.create_user(payload)
        with allure.step("Validate response code and data metadata attributes"):
            assert response.status_code == 201
            data = response.json()
            assert data["name"] == "Alex"
            assert "id" in data