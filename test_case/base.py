from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://afisha.tut.by/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def find_element_by_id(self, id):
        return self.driver.find_element_by_id(id)

    def find_element_by_name(self, name):
        return self.driver.find_element_by_name(name)

    def find_element_by_css_selector(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def find_element_by_link_text(self, link_text):
        return self.driver.find_element_by_link_text(link_text)

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def select_element(self, id, value):
        Select(self.find_element_by_id(id)).select_by_visible_text(value)

    def assert_title(self, title):
        self.assertEqual(title, self.driver.title)

    def go_to(self, link, method='GET'):
        if method == 'GET':
            self.driver.get(link)
        else:
            raise Exception('unsupported')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
