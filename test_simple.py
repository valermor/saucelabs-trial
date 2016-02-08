import unittest

from hamcrest import assert_that, equal_to
from selenium.webdriver.firefox.webdriver import WebDriver

PAGE_LOADING_TIMEOUT = 10
POLLING_INTERVAL = 1
LOGIN_PAGE_URL = 'http://the-internet.herokuapp.com/login'


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = WebDriver()

    def tearDown(self):
        self.driver.quit()

    def test_can_login(self):
        self.driver.get(LOGIN_PAGE_URL)

        login_form = self.driver.find_element_by_id('login')

        assert_that(login_form.is_displayed(), equal_to(True))
