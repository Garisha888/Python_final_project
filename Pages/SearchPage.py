from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):
        self.driver = driver


    def textforinvalidsearch(self):
        invalidtextmessage=self.driver.find_element(By.XPATH,"//div[@class='row']//p").text
        print(invalidtextmessage)
