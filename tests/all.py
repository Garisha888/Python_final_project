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
        searchpage = SearchPage(self.driver,self.wait)
        addincart= AddToCart(self.driver,self.wait)
        checkoutpage=Checkout(self.driver,self.wait)
        homepage.loginclick()
        loginpage.login("demoacc@gmail.com","passdemO1")
        # time.sleep(1)
        homepage.search("shoes")
        addincart.addtocart()
        addincart.add_tocart_from_homepage()
        addincart.deletefromcart()
        # time.sleep(2)
        checkoutpage.checkout_click()
        checkoutpage.checkout_product_list()
        checkoutpage.fill_new_checkout_address("demo", "demoacc@gmail.com", 9840000000, "Sanepa" )
        # time.sleep(2)
        # checkoutpage.fill_new_checkout_address("demo", "demoacc@gmail.com", 9840000000, "lalitpur" )
        # time.sleep(2)
        checkoutpage.delete_checkout_address()
        # time.sleep(2)
        checkoutpage.selectaddress()
        time.sleep(2)
        checkoutpage.finalcheckout()
        time.sleep(2)
        checkoutpage.checkout_details()





