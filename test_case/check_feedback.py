# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from base import BaseTestCase


class CheckFeedbackform(BaseTestCase):
    def test_check_feedbackform(self):
        driver = self.driver
        driver.find_element_by_link_text(u"Сообщение редакции").click()
        driver.find_element_by_id("unews_name").clear()
        driver.find_element_by_id("unews_name").send_keys("TestBot")
        driver.find_element_by_id("unews_phone").clear()
        driver.find_element_by_id("unews_phone").send_keys("+375291234567")
        driver.find_element_by_id("unews_email").clear()
        driver.find_element_by_id("unews_email").send_keys("testbot@selenium.org")
        driver.find_element_by_id("unews_body").clear()
        driver.find_element_by_id("unews_body").send_keys("some test message, \nsorry, support team, it is my lab at the university :)")
        driver.find_element_by_name("submit").click()
