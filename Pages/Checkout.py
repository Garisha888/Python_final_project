import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Checkout:

    def __init__(self, driver):
        self.driver = driver

    def checkout_click(self):
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg btn-block btn-checkout js-checkout']").click()
        # checkoutproducts = self.driver.find_elements(By.XPATH,"//div[@class='checkout-product-detail']//span")


    def checkout_product_list(self):

        print("All Products in cart to checkout:")
        checkoutproducts = self.driver.find_elements(By.XPATH, "//tr[@data-item-added-from='ITEM_DETAILS']")

        for x in checkoutproducts:
            checkoutproductsname = x.find_elements(By.XPATH, "//div[@class='checkout-product-detail']//span")
            checkoutproductsquantity = x.find_elements(By.XPATH, "//td[@class='text-center']")
            checkoutproductsprice = x.find_elements(By.XPATH, "//tr[@data-item-added-from='ITEM_DETAILS']//td[4]")

            length = len(checkoutproductsname)
            for i in range(length):
                print(f"Product Name: {checkoutproductsname[i].text}")
                print(f"Product Quantity: {checkoutproductsquantity[i].text}")
                print(f"Product Price: {checkoutproductsprice[i].text}")

        totalquantity = self.driver.find_element(By.XPATH, "//tbody//th[@class='text-center']")
        print(f"Total Quantity: {totalquantity.text}")

        totalprice = self.driver.find_element(By.XPATH, "//tbody//th[4]")
        print(f"Total Price: {totalprice.text}")

    def fill_new_checkout_address(self, name, email, phoneno, addressline1):
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-add']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "Name").send_keys(name)
        self.driver.find_element(By.ID, "Email").send_keys(email)
        self.driver.find_element(By.ID, "ContactNo").send_keys(phoneno)
        self.driver.find_element(By.ID, "AddressLine1").send_keys(addressline1)
        country_dropdown = Select(self.driver.find_element(By.ID, "CountryID"))
        country_dropdown.select_by_index(0)
        city_dropdown = Select(self.driver.find_element(By.ID, "CityID"))
        city_dropdown.select_by_index(63)
        self.driver.find_element(By.XPATH,"//form[@name='adddeliveryForm']//button[@type='submit']").click()


    def selectaddress(self):
        self.driver.find_element(By.NAME,"ContactID").click()

    def finalcheckout(self):
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-lg btn-primary pull-right']").click()
        time.sleep(2)

    def checkout_details(self):
        allelements=self.driver.find_elements(By.XPATH,"//table[@class='table table-condensed']")
        for x in allelements:
            print(x.text)

    def delete_checkout_address(self):

        self.driver.find_element(By.XPATH, "//i[@class='fa fa-trash']").click()
        time.sleep(2)
        # self.driver.find_element(By.XPATH,"//button[@class='btn btn-danger js-confirm']")
        self.driver.find_element(By.XPATH, "//button[@data-ans='true']").click()
        time.sleep(2)
        alert = self.driver.find_element(By.XPATH, "//div[@class='alertify-notifier ajs-bottom ajs-right']")
        alerttext = alert.text
        print(alerttext)




