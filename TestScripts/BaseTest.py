import pytest
from datetime import datetime


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseTest:
    pass

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "kumar.abhishek" + time_stamp + "@gmail.com"
        






