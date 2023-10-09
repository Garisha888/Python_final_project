import time
from tests.baseTest import baseTest
from Pages.SearchPage import SearchPage
from Pages.LoginPage import LoginPage
from Pages.Homepage import HomePage


class TestLogin(baseTest):


    def test_validlogin1(self):
        homepage = HomePage(self.driver)
        loginpage = LoginPage(self.driver)
        homepage.loginclick()
        loginpage.login("demoacc@gmail.com","passdemO1")

        # time.sleep(2)
        # homepage.search("flower")
        # homepage.addtocart()
        # homepage.addmultipletocart()
        # homepage.deletefromcart()
        # homepage.checkout()
        # time.sleep(10)

    def test_invalidlogin2(self):
        homepage = HomePage(self.driver)
        loginpage = LoginPage(self.driver)
        homepage.loginclick()
        loginpage.login("demoacc@gmail.com","hiii")
        loginpage.invalidlogintext()


    def test_login3(self):
        homepage = HomePage(self.driver)
        loginpage = LoginPage(self.driver)
        homepage.loginclick()
        loginpage.login("","")

    def test_login4(self):
        homepage = HomePage(self.driver)
        loginpage = LoginPage(self.driver)
        homepage.loginclick()
        loginpage.login("demoacc@gmail.com","")

    def test_login5(self):
        homepage = HomePage(self.driver)
        loginpage = LoginPage(self.driver)
        homepage.loginclick()
        loginpage.login("xxxxxxx","")

    def test_validlogin4(self):
        homepage = HomePage(self.driver)
        loginpage = LoginPage(self.driver)
        homepage.loginclick()
        loginpage.login("","hiiiii")





