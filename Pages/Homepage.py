from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def loginclick(self):
        loginbutton = self.driver.find_element(By.XPATH,"//a[@class='user-access profile-link register']")
        loginbutton.click()

    def search(self, searchkey):
        clicksearch = self.driver.find_element(By.XPATH, "//input[@type='text']")
        clicksearch.click()
        clicksearch.clear()
        clicksearch.send_keys(searchkey)
        presssearch = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        presssearch.click()

    def gotocart(self):
        clickcartbutton = self.driver.find_element(By.XPATH, "//li[@class='dropdown cart-dropdown']")
        clickcartbutton.click()

# def deletefromcart(self):
    #     self.driver.find_element(By.XPATH,"//a[@class='fa fa-close table-shopping-remove js-rm-cart']").click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH,"//button[@data-ans='true']").click()
    #     time.sleep(2)
    #     alert = self.driver.find_element(By.XPATH, "//div[@class='alertify-notifier ajs-bottom ajs-right']")
    #     alerttext = alert.text
    #     print(alerttext)
    #     alert = self.driver.switch_to.alert
    #     alertmessage = alert.text()
    #     print(alertmessage)





















