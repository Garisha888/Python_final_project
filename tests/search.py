import time
from tests.baseTest import baseTest
from Pages.SearchPage import SearchPage
from Pages.LoginPage import LoginPage
from Pages.Homepage import HomePage


class TestSearch(baseTest):

    def test_searchvalid(self):
        homepage = HomePage(self.driver)
        homepage.search("flower")

    def test_searchinvalid(self):
        homepage = HomePage(self.driver)
        searchpage = SearchPage(self.driver)
        homepage.search("honda")
        time.sleep(5)
        searchpage.textforinvalidsearch()

    def test_loginvalidsearch(self):
        homepage = HomePage(self.driver)
        loginpage = LoginPage(self.driver)
        homepage.loginclick()
        loginpage.login("demoacc@gmail.com", "passdemO1")
        homepage.search("flower")
        time.sleep(5)

    def test_logininvalidsearch(self):
        homepage = HomePage(self.driver)
        loginpage = LoginPage(self.driver)
        searchpage = SearchPage(self.driver)
        homepage.loginclick()
        loginpage.login("demoacc@gmail.com", "passdemO1")
        homepage.search("honda")
        time.sleep(5)
        searchpage.textforinvalidsearch()
