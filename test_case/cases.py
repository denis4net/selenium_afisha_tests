# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select
import time
import re

from base import BaseTestCase


class CheckFeedbackformTestCase(BaseTestCase):
    def run_test(self):
        self.find_element_by_link_text(u"Сообщение редакции").click()
        self.find_element_by_id("unews_name").clear()
        self.find_element_by_id("unews_name").send_keys("TestBot")
        self.find_element_by_id("unews_phone").clear()
        self.find_element_by_id("unews_phone").send_keys("+375291234567")
        self.find_element_by_id("unews_email").clear()
        self.find_element_by_id("unews_email").send_keys("testbot@selenium.org")
        self.find_element_by_id("unews_body").clear()
        self.find_element_by_id("unews_body").send_keys("some test message, \nsorry, support team, it is my lab at the university :)")
        self.find_element_by_name("submit").click()


class CheckHomePageGroupsTestCase(BaseTestCase):
    def run_test(self):
        self.go_to(self.base_url + "/")
        self.assertEqual(u"Куда сходить сегодня", self.find_element_by_link_text(u"Куда сходить сегодня").text)
        self.assertEqual(u"Самое интересное скоро", self.find_element_by_css_selector("h2.title_block").text)
        self.assertEqual(u"Смотрите онлайн бесплатно", self.find_element_by_css_selector("div.title_block").text)
        self.assertEqual(u"Новости", self.find_element_by_css_selector(u"a[title=\"Все новости\"]").text)
        self.assertEqual(u"Фотоотчёты", self.find_element_by_link_text(u"Фотоотчёты").text)


class CheckLinksTestCase(BaseTestCase):
    def run_test(self):
        self.go_to(self.base_url + "/")
        self.find_element_by_link_text(u"Кино").click()
        self.assert_title(u"Кинотеатры Минска - Киноафиша кинотеатров на сегодня - Купить билеты в кино онлайн в Минске | AFISHA.TUT.BY")
        self.find_element_by_link_text(u"Концерты").click()
        self.assert_title(u"Афиша концертов - все концерты Минска | AFISHA.TUT.BY")
        self.find_element_by_link_text(u"Вечеринки").click()
        self.assert_title(u"Афиша вечеринок Минска - все вечеринки и дискотеки в Минске | AFISHA.TUT.BY")
        self.find_element_by_link_text(u"Спектакли").click()
        self.assert_title(u"Афиша театров - Театральная афиша Минска | AFISHA.TUT.BY")
        self.find_element_by_link_text(u"Выставки").click()
        self.assert_title(u"Выставки Минска - Афиша выставок | AFISHA.TUT.BY")
        self.find_element_by_link_text(u"Цирк").click()
        self.assert_title(u"Афиша цирка в Минске - Билеты в цирк в Минске, афиша цирковых представлений - AFISHA.TUT.BY")
        self.find_element_by_link_text(u"Детям").click()
        self.assert_title(u"Куда пойти с ребенком в Минске - Афиша для детей в Минске | AFISHA.TUT.BY")
        self.go_to(self.base_url + "/")


class CheckMobileVersionTestCase(BaseTestCase):
    def run_test(self):
        self.go_to(self.base_url + "/")
        self.find_element_by_link_text(u"Версия для смартфонов").click()
        self.assertRegexpMatches(self.find_element_by_xpath("//div[@id='content']/ul/li[3]/a").text, r"^Концерты[\s\S]*$")
        self.assertRegexpMatches(self.find_element_by_xpath("//div[@id='content']/ul/li[4]/a").text, r"^Вечеринки[\s\S]*$")
        self.assertRegexpMatches(self.find_element_by_xpath("//div[@id='content']/ul/li[5]/a").text, r"^Спектакли[\s\S]*$")
        self.assertRegexpMatches(self.find_element_by_xpath("//div[@id='content']/ul/li[6]/a").text, r"^Выставки[\s\S]*$")
        self.assertRegexpMatches(self.find_element_by_xpath("//div[@id='content']/ul/li[8]/a").text, r"Др\. события.*")
        self.assertRegexpMatches(self.find_element_by_xpath("//div[@id='content']/ul/li[9]/a").text, r"Афиша для детей.*")
        self.assertRegexpMatches(self.find_element_by_xpath("//div[@id='content']/ul/li[11]/a").text, r"Рестораны и кафе.*")
        self.find_element_by_link_text(u"Полная версия").click()


class CheckSigninTestCase(BaseTestCase):
    def run_test(self):
        self.go_to(self.base_url + "/")
        self.find_element_by_link_text(u"Вход").click()
        self.find_element_by_name("login").clear()
        self.find_element_by_name("login").send_keys("zasajo@yhg.biz")
        self.find_element_by_name("password").clear()
        self.find_element_by_name("password").send_keys("somepassword2015")
        self.find_element_by_css_selector("input.button").click()
        self.assertEqual("SomeName SomeSecondName", self.find_element_by_link_text("SomeName SomeSecondName").text)
        self.find_element_by_link_text(u"Выйти").click()


class CheckSigninIncorrectPasswordTestCase(BaseTestCase):
    def run_test(self):
        self.go_to(self.base_url + "/?trnd=81065")
        self.find_element_by_link_text(u"Вход").click()
        self.find_element_by_name("login").clear()
        self.find_element_by_name("login").send_keys("somemail@selenium.org")
        self.find_element_by_name("password").clear()
        self.find_element_by_name("password").send_keys("somepassword")
        self.find_element_by_css_selector("input.button").click()
        self.assertEqual(u"Неверное имя пользователя или пароль", self.find_element_by_css_selector("div.b-auth__error").text)


class CheckSmartphoneVersionTestCase(BaseTestCase):
    def run_test(self):
        self.go_to(self.base_url + "/")
        self.find_element_by_link_text(u"Версия для смартфонов").click()
        self.assertRegexpMatches(self.find_element_by_xpath("//div[@id='content']/ul/li[3]/a").text, r"^Концерты[\s\S]*$")
        self.assertRegexpMatches(self.find_element_by_xpath("//div[@id='content']/ul/li[4]/a").text, r"^Вечеринки[\s\S]*$")
        self.assertRegexpMatches(self.find_element_by_xpath("//div[@id='content']/ul/li[5]/a").text, r"^Спектакли[\s\S]*$")
        self.assertRegexpMatches(self.find_element_by_xpath("//div[@id='content']/ul/li[6]/a").text, r"^Выставки[\s\S]*$")
        self.assertRegexpMatches(self.find_element_by_xpath("//div[@id='content']/ul/li[8]/a").text, r"Др\. события.*")
        self.assertRegexpMatches(self.find_element_by_xpath("//div[@id='content']/ul/li[9]/a").text, r"Афиша для детей.*")
        self.assertRegexpMatches(self.find_element_by_xpath("//div[@id='content']/ul/li[11]/a").text, r"Рестораны и кафе.*")
        self.find_element_by_link_text(u"Полная версия").click()


class RegisterUserTestCase(BaseTestCase):
    def run_test(self):
        self.go_to(self.base_url + "/")
        self.find_element_by_link_text(u"Регистрация").click()
        self.find_element_by_id("FirstName").clear()
        self.find_element_by_id("FirstName").send_keys("SomeName")
        self.find_element_by_id("notMailGogle").click()
        self.find_element_by_xpath("//table[@id='tblFirstStep']/tbody/tr/td/label[2]").click()
        self.find_element_by_id("SecondName").clear()
        self.find_element_by_id("SecondName").send_keys("SomeSecondName")
        self.find_element_by_id("Username").clear()
        self.find_element_by_id("Username").send_keys("somemail@selenium.org")
        self.find_element_by_id("Password1").clear()
        self.find_element_by_id("Password1").send_keys("somepassword2015")
        self.find_element_by_id("Password2").clear()
        self.find_element_by_id("Password2").send_keys("somepassword2015")
        self.select_element("_3_1", u"1")
        self.select_element("_3_2", u"января")
        self.select_element("_3_3", "1992")
        self.find_element_by_id("msex").click()
        self.find_element_by_id("city_div0").clear()
        self.find_element_by_id("city_div0").send_keys("SomeCity")
        self.find_element_by_id("Answer").clear()
        self.find_element_by_id("Answer").send_keys("SomeSurname2")
        self.find_element_by_id("ForgotPasswordPhone").clear()
        self.find_element_by_id("ForgotPasswordPhone").send_keys("+375291234567")
        self.find_element_by_id("_14").click()
        self.find_element_by_id("reg_btn").click()
        self.find_element_by_id("city_div0").clear()
        self.find_element_by_id("city_div0").send_keys("")
        self.assertEqual(u"Не введено слово на картинке", self.find_element_by_id("idCodeMessage").text)


def get_tests():
    return ([name for name in globals() if name.endswith('TestCase')])
