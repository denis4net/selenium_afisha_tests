# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class RegisterUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://afisha.tut.by/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_register_user(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Регистрация").click()
        driver.find_element_by_id("FirstName").clear()
        driver.find_element_by_id("FirstName").send_keys("SomeName")
        driver.find_element_by_id("notMailGogle").click()
        driver.find_element_by_xpath("//table[@id='tblFirstStep']/tbody/tr/td/label[2]").click()
        driver.find_element_by_id("SecondName").clear()
        driver.find_element_by_id("SecondName").send_keys("SomeSecondName")
        driver.find_element_by_id("Username").clear()
        driver.find_element_by_id("Username").send_keys("somemail@selenium.org")
        driver.find_element_by_id("Password1").clear()
        driver.find_element_by_id("Password1").send_keys("somepassword2015")
        driver.find_element_by_id("Password2").clear()
        driver.find_element_by_id("Password2").send_keys("somepassword2015")
        Select(driver.find_element_by_id("_3_1")).select_by_visible_text("1")
        Select(driver.find_element_by_id("_3_2")).select_by_visible_text(u"января")
        Select(driver.find_element_by_id("_3_3")).select_by_visible_text("1992")
        driver.find_element_by_id("msex").click()
        driver.find_element_by_id("city_div0").clear()
        driver.find_element_by_id("city_div0").send_keys("SomeCity")
        driver.find_element_by_id("Answer").clear()
        driver.find_element_by_id("Answer").send_keys("SomeSurname2")
        driver.find_element_by_id("ForgotPasswordPhone").clear()
        driver.find_element_by_id("ForgotPasswordPhone").send_keys("+375291234567")
        driver.find_element_by_id("_14").click()
        driver.find_element_by_id("reg_btn").click()
        driver.find_element_by_id("city_div0").clear()
        driver.find_element_by_id("city_div0").send_keys("")
        self.assertEqual(u"Не введено слово на картинке", driver.find_element_by_id("idCodeMessage").text)
    
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
