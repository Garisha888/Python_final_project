from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):

        inputusername = self.driver.find_element(By.ID, "Username")
        inputusername.send_keys(username)
        inputpassword = self.driver.find_element(By.ID, "Password")
        inputpassword.send_keys(password)
        loginbutton = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        loginbutton.click()

    def invalidlogintext(self):
        invalidtextmessage = self.driver.find_element(By.XPATH,"//div[@class='card-content white-text']//p").text
        print(invalidtextmessage)
