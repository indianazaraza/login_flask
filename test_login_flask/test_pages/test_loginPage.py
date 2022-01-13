import pytest
from test_login_flask.pages.loginPage import LoginPage


@pytest.mark.usefixtures("setup")
class TestLoginPage:
    def test_title_before_login(self) -> None:
        """Test current web page title before login"""
        assert LoginPage(self.driver).title_web_page() == "Login"

    def test_login_user(self) -> None:
        LoginPage(self.driver).login_user()

    def test_title_after_login(self) -> None:
        """Test current web page title after login"""
        assert LoginPage(self.driver).title_web_page() == "Info"
