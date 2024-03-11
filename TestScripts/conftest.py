import allure
import pytest
import logging
from allure_commons.types import AttachmentType
from selenium import webdriver
from io import StringIO

from Utilities.config_utility import ConfigUtility
import Utilities.logger_utility as log_utils

# Adding logger
log = log_utils.custom_logger(logging.INFO)


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)
        log.error(f"Test failed: {item.name}")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    if rep.failed:
        log.error(f"Test failed: {item.name}")


@pytest.fixture()
def setup_and_teardown(request):
    log.info("Setting up test...")
    setup_logs_stream = StringIO()
    setup_handler = logging.StreamHandler(setup_logs_stream)
    log.addHandler(setup_handler)

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
        log.error("Provide a valid browser name from this list chrome/firefox/edge")

    driver.maximize_window()
    app_url = config_utility.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    log.info(f"Test setup completed. Browser: {browser}, URL: {app_url}")

    yield

    allure.attach(setup_logs_stream.getvalue(), name="setup_logs", attachment_type=AttachmentType.TEXT)
    setup_handler.close()
    log.removeHandler(setup_handler)

    driver.quit()
    log.info("Test teardown completed.")
