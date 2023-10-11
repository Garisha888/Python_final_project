import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


class Checkout:

    def __init__(self, driver,wait):
        self.driver = driver
        self.wait = wait

    def checkout_click(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-primary btn-lg btn-block btn-checkout js-checkout']"))).click()
        # checkoutproducts = self.driver.find_elements(By.XPATH,"//div[@class='checkout-product-detail']//span")


    def checkout_product_list(self):

        print("All Products in cart to checkout:")
        checkoutproducts =self.driver.find_elements(By.XPATH, "//tr[@data-item-added-from='ITEM_DETAILS']")

        for x in checkoutproducts:
            checkoutproductsname = x.find_elements(By.XPATH, "//div[@class='checkout-product-detail']//span")
            checkoutproductsquantity = x.find_elements(By.XPATH, "//td[@class='text-center']")
            checkoutproductsprice = x.find_elements(By.XPATH, "//tr[@data-item-added-from='ITEM_DETAILS']//td[4]")

            length = len(checkoutproductsname)
            for i in range(length):
                print(f"Product Name: {checkoutproductsname[i].text}")
                print(f"Product Quantity: {checkoutproductsquantity[i].text}")
                print(f"Product Price: {checkoutproductsprice[i].text}")

        totalquantity =  self.wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody//th[@class='text-center']")))
        print(f"Total Quantity: {totalquantity.text}")

        totalprice =  self.wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody//th[4]")))
        print(f"Total Price: {totalprice.text}")

    def fill_new_checkout_address(self, name, email, phoneno, addressline1):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-add']"))).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.ID, "Name"))).send_keys(name)
        self.wait.until(EC.element_to_be_clickable((By.ID, "Email"))).send_keys(email)
        self.wait.until(EC.element_to_be_clickable((By.ID, "ContactNo"))).send_keys(phoneno)
        self.wait.until(EC.element_to_be_clickable((By.ID, "AddressLine1"))).send_keys(addressline1)
        country_dropdown = Select(self.wait.until(EC.element_to_be_clickable((By.ID, "CountryID"))))
        country_dropdown.select_by_index(0)
        city_dropdown = Select(self.wait.until(EC.element_to_be_clickable((By.ID, "CityID"))))
        city_dropdown.select_by_index(63)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//form[@name='adddeliveryForm']//button[@type='submit']"))).click()


    def selectaddress(self):
        self.wait.until(EC.element_to_be_clickable((By.NAME,"ContactID"))).click()

    def finalcheckout(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='btn btn-lg btn-primary pull-right']"))).click()
        time.sleep(2)

    def checkout_details(self):
        allelements= self.driver.find_elements(By.XPATH,"//table[@class='table table-condensed']")
        for x in allelements:
            print(x.text)

    def delete_checkout_address(self):

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-trash']"))).click()
        time.sleep(2)
        # self.driver.find_element(By.XPATH,"//button[@class='btn btn-danger js-confirm']")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-ans='true']"))).click()
        time.sleep(2)
        alert =  self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='alertify-notifier ajs-bottom ajs-right']")))
        alerttext = alert.text
        print(alerttext)




