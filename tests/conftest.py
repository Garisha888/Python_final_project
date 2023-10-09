import pytest
from selenium import webdriver


@pytest.fixture()
def setup_teardown(request):
    driver = webdriver.Chrome()
    driver.get("https://muncha.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
