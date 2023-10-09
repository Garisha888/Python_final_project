import time
from tests.baseTest import baseTest
from Pages.SearchPage import SearchPage
from Pages.LoginPage import LoginPage
from Pages.Homepage import HomePage
from Pages.AddToCart import AddToCart
from Pages.Checkout import Checkout


class TestAll(baseTest):


    def test_all(self):
        homepage = HomePage(self.driver)
        loginpage = LoginPage(self.driver)
        checkoutpage=Checkout(self.driver)
        homepage.loginclick()
        loginpage.login("demoacc@gmail.com","passdemO1")
        time.sleep(1)
        homepage.gotocart()
        checkoutpage.checkout_click()
        checkoutpage.checkout_product_list()
        checkoutpage.fill_new_checkout_address("demo", "demoacc@gmail.com", 9840000000, "Sanepa" )
        time.sleep(2)
        # checkoutpage.delete_checkout_address()
        checkoutpage.selectaddress()
        time.sleep(2)
        checkoutpage.finalcheckout()
        time.sleep(2)
        checkoutpage.checkout_details()


