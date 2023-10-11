import time
from tests.baseTest import baseTest
from Pages.SearchPage import SearchPage
from Pages.LoginPage import LoginPage
from Pages.Homepage import HomePage


class TestSearch(baseTest):

    def test_searchvalid(self):
        homepage = HomePage(self.driver,self.wait)
        homepage.search("flower")

    def test_searchinvalid(self):
        homepage = HomePage(self.driver,self.wait)
        searchpage = SearchPage(self.driver,self.wait)
        homepage.search("honda")
        time.sleep(5)
        searchpage.textforinvalidsearch()

    def test_loginvalidsearch(self):
        homepage = HomePage(self.driver,self.wait)
        loginpage = LoginPage(self.driver,self.wait)
        homepage.loginclick()
        loginpage.login("demoacc@gmail.com", "passdemO1")
        homepage.search("flower")
        time.sleep(5)

    def test_logininvalidsearch(self):
        homepage = HomePage(self.driver,self.wait)
        loginpage = LoginPage(self.driver,self.wait)
        searchpage = SearchPage(self.driver,self.wait)
        homepage.loginclick()
        loginpage.login("demoacc@gmail.com", "passdemO1")
        homepage.search("honda")
        time.sleep(5)
        searchpage.textforinvalidsearch()
