# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CheckMobileVersion(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://afisha.tut.by/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_check_mobile_version(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Версия для смартфонов").click()
        self.assertRegexpMatches(driver.find_element_by_xpath("//div[@id='content']/ul/li[3]/a").text, r"^Концерты[\s\S]*$")
        self.assertRegexpMatches(driver.find_element_by_xpath("//div[@id='content']/ul/li[4]/a").text, r"^Вечеринки[\s\S]*$")
        self.assertRegexpMatches(driver.find_element_by_xpath("//div[@id='content']/ul/li[5]/a").text, r"^Спектакли[\s\S]*$")
        self.assertRegexpMatches(driver.find_element_by_xpath("//div[@id='content']/ul/li[6]/a").text, r"^Выставки[\s\S]*$")
        self.assertRegexpMatches(driver.find_element_by_xpath("//div[@id='content']/ul/li[8]/a").text, r"Др\. события.*")
        self.assertRegexpMatches(driver.find_element_by_xpath("//div[@id='content']/ul/li[9]/a").text, r"Афиша для детей.*")
        self.assertRegexpMatches(driver.find_element_by_xpath("//div[@id='content']/ul/li[11]/a").text, r"Рестораны и кафе.*")
        driver.find_element_by_link_text(u"Полная версия").click()
    
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
