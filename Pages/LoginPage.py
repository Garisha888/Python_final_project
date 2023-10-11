from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver,wait):
        self.driver = driver
        self.wait = wait

    def login(self, username, password):

        inputusername = self.wait.until(EC.element_to_be_clickable((By.ID, "Username")))
        inputusername.send_keys(username)
        inputpassword = self.wait.until(EC.element_to_be_clickable((By.ID, "Password")))
        inputpassword.send_keys(password)
        loginbutton = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        loginbutton.click()

    def invalidlogintext(self):
        invalidtextmessage = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='card-content white-text']//p"))).text
        print(invalidtextmessage)
