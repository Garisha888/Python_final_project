import time

from tests.baseTest import baseTest
from Pages.LoginPage import LoginPage
from Pages.Homepage import HomePage
from Pages.AddToCart import AddToCart



class TestCart(baseTest):


    def test_cart(self):
        homepage = HomePage(self.driver)
        loginpage = LoginPage(self.driver)
        addincart= AddToCart(self.driver)
        homepage.loginclick()
        loginpage.login("demoacc@gmail.com","passdemO1")
        # time.sleep(2)
        homepage.search("shoes")
        addincart.addtocart()
        addincart.deletefromcart()


