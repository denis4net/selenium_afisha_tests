# -*- coding: utf-8 -*-
import time
import re

from base import BaseTestCase


class CheckFeedbackform(BaseTestCase):
    def run_test(self):
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


class CheckHomePageGroups(BaseTestCase):
    def run_test(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        self.assertEqual(u"Куда сходить сегодня", driver.find_element_by_link_text(u"Куда сходить сегодня").text)
        self.assertEqual(u"Самое интересное скоро", driver.find_element_by_css_selector("h2.title_block").text)
        self.assertEqual(u"Смотрите онлайн бесплатно", driver.find_element_by_css_selector("div.title_block").text)
        self.assertEqual(u"Новости", driver.find_element_by_css_selector(u"a[title=\"Все новости\"]").text)
        self.assertEqual(u"Фотоотчёты", driver.find_element_by_link_text(u"Фотоотчёты").text)


class CheckLinks(BaseTestCase):
    def run_test(self):
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


class CheckMobileVersion(BaseTestCase):
    def run_test(self):
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


class CheckSignin(BaseTestCase):
    def run_test(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход").click()
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("zasajo@yhg.biz")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("somepassword2015")
        driver.find_element_by_css_selector("input.button").click()
        self.assertEqual("SomeName SomeSecondName", driver.find_element_by_link_text("SomeName SomeSecondName").text)
        driver.find_element_by_link_text(u"Выйти").click()


class CheckSigninIncorrectPassword(BaseTestCase):
    def run_test(self):
        driver = self.driver
        driver.get(self.base_url + "/?trnd=81065")
        driver.find_element_by_link_text(u"Вход").click()
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("somemail@selenium.org")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("somepassword")
        driver.find_element_by_css_selector("input.button").click()
        self.assertEqual(u"Неверное имя пользователя или пароль", driver.find_element_by_css_selector("div.b-auth__error").text)


class CheckSmartphoneVersion(BaseTestCase):
    def run_test(self):
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


class RegisterUser(BaseTestCase):
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


def get_tests():
    return (set(globals()))
