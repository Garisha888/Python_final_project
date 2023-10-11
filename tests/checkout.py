import time
from tests.baseTest import baseTest
from Pages.SearchPage import SearchPage
from Pages.LoginPage import LoginPage
from Pages.Homepage import HomePage
from Pages.AddToCart import AddToCart
from Pages.Checkout import Checkout


class TestAll(baseTest):


    def test_all(self):
        homepage = HomePage(self.driver,self.wait)
        loginpage = LoginPage(self.driver,self.wait)
        checkoutpage=Checkout(self.driver,self.wait)
        homepage.loginclick()
        loginpage.login("demoacc@gmail.com","passdemO1")
        homepage.gotocart()
        checkoutpage.checkout_click()
        checkoutpage.checkout_product_list()
        # time.sleep(3)
        # checkoutpage.fill_new_checkout_address("demo", "demoacc@gmail.com", 9840000000, "Sanepa" )
        # time.sleep(2)
        checkoutpage.delete_checkout_address()
        checkoutpage.selectaddress()
        # time.sleep(2)
        checkoutpage.finalcheckout()
        # time.sleep(2)
        checkoutpage.checkout_details()


