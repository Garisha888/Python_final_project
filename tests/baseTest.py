import pytest


@pytest.mark.usefixtures("setup_teardown")
class baseTest:
    pass
    # def __init__(self , driver):
    #     self.driver = driver
    #     pass