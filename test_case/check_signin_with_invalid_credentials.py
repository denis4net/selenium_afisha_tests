# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CheckSigninIncorrectPassword(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://afisha.tut.by/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_check_signin_incorrect_password(self):
        driver = self.driver
        driver.get(self.base_url + "/?trnd=81065")
        driver.find_element_by_link_text(u"Вход").click()
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("somemail@selenium.org")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("somepassword")
        driver.find_element_by_css_selector("input.button").click()
        self.assertEqual(u"Неверное имя пользователя или пароль", driver.find_element_by_css_selector("div.b-auth__error").text)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
