import time
from selenium.webdriver.common.by import By
from Pages.Homepage import HomePage as homepage
from selenium.webdriver.support import expected_conditions as EC


class AddToCart:



    def __init__(self, driver,wait):
        self.driver = driver
        self.wait = wait

    def addtocart(self):

        clickitem = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='product-link']")))
        clickitem.click()
        #increase item
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='product-page-qty product-page-qty-minus']"))).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='product-page-qty product-page-qty-minus']"))).click()
        time.sleep(1)
        #decrease item
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='product-page-qty product-page-qty-plus']"))).click()
        time.sleep(1)
        #itemname
        item = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@class="description-note"]//h3')))
        itemname=item.text
        print(itemname)

        addcart = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='btn btn-lg btn-warning js-ga-cart-btn']")))
        addcart.click()
        time.sleep(1)

        alert = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='alertify-notifier ajs-bottom ajs-right']")))
        alerttext=alert.text
        print(alerttext)
        homepage.gotocart(self)

#if not logged in we cannot delete
    def deletefromcart(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='fa fa-close table-shopping-remove js-rm-cart']"))).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@data-ans='true']"))).click()
        time.sleep(2)

        alert = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='alertify-notifier ajs-bottom ajs-right']")))
        alerttext = alert.text
        print(alerttext)


        # alert = self.driver.switch_to.alert
        # alertmessage = alert.text()
        # print(alertmessage)



    def add_tocart_from_homepage(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Muncha.com.np']"))).click()
        time.sleep(1)
        self.addtocart()