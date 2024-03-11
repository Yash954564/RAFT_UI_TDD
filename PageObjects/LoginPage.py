from selenium.common.exceptions import NoSuchElementException
from SupportLibraries.base_helper import BaseHelpers
import allure

class LoginPage(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)

    username = "//input[@placeholder='Username']"
    password = "//input[@placeholder='Password']"
    submit_button = "//button[normalize-space()='Login']"

    @allure.step("Enter username: {1}")
    def enter_username(self, uname):
        try:
            allure.attach(self.driver.get_screenshot_as_png(), name="enter_username_screenshot", attachment_type=allure.attachment_type.PNG)
            return self.enter_text_action(uname, self.username)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="enter_username_error_screenshot", attachment_type=allure.attachment_type.PNG)
            allure.step(f"An element was not found: {e}")
            allure.step("Step failed.", status=allure.attachment_type.FAIL)
            raise  # Re-raise the exception after handling if necessary

    @allure.step("Enter password")
    def enter_password(self, passwd):
        try:
            allure.attach(self.driver.get_screenshot_as_png(), name="enter_password_screenshot", attachment_type=allure.attachment_type.PNG)
            return self.enter_text_action(passwd, self.password)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="enter_password_error_screenshot", attachment_type=allure.attachment_type.PNG)
            allure.step(f"An element was not found: {e}")
            allure.step("Step failed.", status=allure.attachment_type.FAIL)
            raise  # Re-raise the exception after handling if necessary

    @allure.step("Click Login button")
    def click_login_button(self):
        try:
            allure.attach(self.driver.get_screenshot_as_png(), name="click_login_button_screenshot", attachment_type=allure.attachment_type.PNG)
            return self.mouse_click_action(self.submit_button)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="click_login_button_error_screenshot", attachment_type=allure.attachment_type.PNG)
            allure.step(f"An element was not found: {e}")
            allure.step("Step failed.", status=allure.attachment_type.FAIL)
            raise  # Re-raise the exception after handling if necessary

    @allure.step("Login to application with username: {1} and password: {2}")
    def login_to_application(self, email_address_text, password_text):
        try:
            self.enter_username(email_address_text)
            self.enter_password(password_text)
            return self.click_login_button()
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="login_error_screenshot", attachment_type=allure.attachment_type.PNG)
            allure.step(f"An element was not found during login: {e}")
            allure.step("Step failed.", status=allure.attachment_type.FAIL)
            raise  # Re-raise the exception after handling if necessary
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="login_error_screenshot", attachment_type=allure.attachment_type.PNG)
            allure.step(f"An unexpected error occurred during login: {e}")
            allure.step("Step failed.", status=allure.attachment_type.FAIL)
            raise  # Re-raise the exception after handling if necessary
