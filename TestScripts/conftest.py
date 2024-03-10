import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from Utilities.config_utility import ConfigUtility

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture()
def setup_and_teardown(request):
    config_utility = ConfigUtility()
    browser = config_utility.read_configuration("basic info", "browser")
    global driver
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")

    driver.maximize_window()
    app_url = config_utility.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
