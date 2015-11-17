# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CheckLinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://afisha.tut.by/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_check_links(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Кино").click()
        try: self.assertEqual(u"Кинотеатры Минска - Киноафиша кинотеатров на сегодня - Купить билеты в кино онлайн в Минске | AFISHA.TUT.BY", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text(u"Концерты").click()
        try: self.assertEqual(u"Афиша концертов - все концерты Минска | AFISHA.TUT.BY", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text(u"Вечеринки").click()
        try: self.assertEqual(u"Афиша вечеринок Минска - все вечеринки и дискотеки в Минске | AFISHA.TUT.BY", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text(u"Спектакли").click()
        try: self.assertEqual(u"Афиша театров - Театральная афиша Минска | AFISHA.TUT.BY", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text(u"Выставки").click()
        for i in range(60):
            try:
                if u"Выставки Минска - Афиша выставок | AFISHA.TUT.BY" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_link_text(u"Цирк").click()
        try: self.assertEqual(u"Афиша цирка в Минске - Билеты в цирк в Минске, афиша цирковых представлений - AFISHA.TUT.BY", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text(u"Детям").click()
        try: self.assertEqual(u"Куда пойти с ребенком в Минске - Афиша для детей в Минске | AFISHA.TUT.BY", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.get(self.base_url + "/")
    
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
