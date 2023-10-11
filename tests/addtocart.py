import time

from tests.baseTest import baseTest
from Pages.LoginPage import LoginPage
from Pages.Homepage import HomePage
from Pages.AddToCart import AddToCart



class TestCart(baseTest):


    def test_cart(self):
        homepage = HomePage(self.driver,self.wait)
        loginpage = LoginPage(self.driver,self.wait)
        addincart= AddToCart(self.driver,self.wait)
        homepage.loginclick()
        loginpage.login("demoacc@gmail.com","passdemO1")
        # time.sleep(2)
        homepage.search("shoes")
        addincart.addtocart()
        addincart.deletefromcart()


