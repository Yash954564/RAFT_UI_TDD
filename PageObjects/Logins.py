from selenium.common.exceptions import NoSuchElementException
from SupportLibraries.base_helper import BaseHelpers

class LoginPaged(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)

    username = "//input[@placeholder='Username']"
    password = "//input[@placeholder='Password']"
    submit_button = "//button[normalize-space()='Login']"

    def enter_username(self, uname):
        try:
            return self.enter_text_action(uname, self.username)
        except NoSuchElementException as e:
            print(f"An element was not found: {e}")
            # Handle the exception as per your requirements
            raise  # Re-raise the exception after handling if necessary

    def enter_password(self, passwd):
        try:
            return self.enter_text_action(passwd, self.password)
        except NoSuchElementException as e:
            print(f"An element was not found: {e}")
            # Handle the exception as per your requirements
            raise  # Re-raise the exception after handling if necessary

    def click_login_button(self):
        try:
            return self.mouse_click_action(self.submit_button)
        except NoSuchElementException as e:
            print(f"An element was not found: {e}")
            # Handle the exception as per your requirements
            raise  # Re-raise the exception after handling if necessary

    def login_to_application(self, email_address_text, password_text):
        try:
            self.enter_username(email_address_text)
            self.enter_password(password_text)
            return self.click_login_button()
        except NoSuchElementException as e:
            print(f"An element was not found during login: {e}")
            # Handle the exception as per your requirements
            raise  # Re-raise the exception after handling if necessary
        except Exception as e:
            print(f"An unexpected error occurred during login: {e}")
            # Handle the exception as per your requirements
            raise  # Re-raise the exception after handling if necessary