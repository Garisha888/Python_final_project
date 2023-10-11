import pytest
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def setup_teardown(request):

    try:
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        driver.get("https://muncha.com/")
        driver.maximize_window()
        request.cls.driver = driver
        request.cls.wait = wait
        yield
        driver.quit()

    except WebDriverException as g:
        print(f"an error had occured:: {str(g)}")

    except Exception as e:
        print(f"an error had occured:: {str(e)}")
