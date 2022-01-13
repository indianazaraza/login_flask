from test_login_flask.base.basePage import BasePage
from test_login_flask.base.locators import Locators


class LoginPage(BasePage):
    """Class containing the login functions"""
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def fill_form(self) -> None:
        """Fills the form login"""
        self.send_to(Locators.username_field, "admin")
        self.send_to(Locators.password_field, "1565")

    def login_user(self) -> None:
        """Login for a user"""
        if self.is_displayed(Locators.form_login):
            self.fill_form()
            self.click(Locators.login_button)
