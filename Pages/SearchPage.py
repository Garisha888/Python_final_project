from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class SearchPage:

    def __init__(self, driver,wait):
        self.driver = driver
        self.wait = wait


    def textforinvalidsearch(self):
        invalidtextmessage= self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='row']//p"))).text
        print(invalidtextmessage)
