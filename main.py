# -*- coding: utf-8 -*-

import unittest
from test_case.base import BaseTestCase


class CheckFeedbackform(BaseTestCase):
    def test_checkfeedbackform(self):
        self.go_to(self.base_url + "/")
        self.find_element_by_link_text(u"Сообщение редакции").click()
        self.input("unews_name", "TestBot")
        self.input("unews_phone", "+375291234567")
        self.input("unews_email", "testbot@selenium.org")
        self.input("unews_body", "some test message, \nsorry, support team, it is my lab at the university :)")
        self.find_element_by_name("submit").click()


class CheckHomePageGroups(BaseTestCase):
    def test_check_home_page_groups(self):
        self.go_to(self.base_url + "/")
        self.assertEqual(u"Куда сходить сегодня и завтра", self.find_element_by_link_text(u"Куда сходить сегодня и завтра").text)
        self.assertEqual(u"Самое интересное скоро", self.find_element_by_css_selector("h2.title_block").text)
        self.assertEqual(u"Смотрите онлайн бесплатно", self.find_element_by_css_selector("div.title_block").text)
        self.assertEqual(u"Новости", self.find_element_by_css_selector(u"a[title=\"Все новости\"]").text)
        self.assertEqual(u"Фотоотчёты", self.find_element_by_link_text(u"Фотоотчёты").text)


class CheckLinks(BaseTestCase):
    def test_check_links(self):
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


class CheckMobileVersion(BaseTestCase):
    def test_check_mobile_version(self):
        self.go_to(self.base_url + "/")
        self.find_element_by_link_text(u"Мобильная версия").click()
        self.assertEqual(u"Кино", self.find_element_by_link_text(u"Кино").text)
        self.assertEqual(u"Театры", self.find_element_by_link_text(u"Театры").text)
        self.assertEqual(u"Концерты", self.find_element_by_link_text(u"Концерты").text)
        self.assertEqual(u"Вечеринки", self.find_element_by_link_text(u"Вечеринки").text)
        self.assertEqual(u"Выставки", self.find_element_by_link_text(u"Выставки").text)
        self.assertEqual(u"Цирк", self.find_element_by_link_text(u"Цирк").text)
        self.find_element_by_link_text(u"Полная версия").click()


class CheckSignin(BaseTestCase):
    def test_check_signin(self):
        self.go_to(self.base_url + "/")
        self.find_element_by_link_text(u"Вход").click()
        self.input(name="login", value="zasajo@yhg.biz")
        self.input(name="password", value="somepassword2015")
        self.find_element_by_css_selector("input.button").click()
        self.assertEqual("SomeName SomeSecondName", self.find_element_by_link_text("SomeName SomeSecondName").text)
        self.find_element_by_link_text(u"Выйти").click()


class CheckSigninIncorrectPassword(BaseTestCase):
    def test_check_signin_incorrect_password(self):
        self.go_to(self.base_url + "/?trnd=81065")
        self.find_element_by_link_text(u"Вход").click()
        self.input(name="login", value="somemail@selenium.org")
        self.input(name="password", value="somepassword")
        self.find_element_by_css_selector("input.button").click()
        self.assertEqual(u"Неверное имя пользователя или пароль", self.find_element_by_css_selector("div.b-auth__error").text)


class CheckSmartphoneVersion(BaseTestCase):
    def test_check_smartphone_version(self):
        self.go_to(self.base_url + "/")
        self.find_element_by_link_text(u"Мобильная версия").click()
        self.assertEqual(u"Кино", self.find_element_by_link_text(u"Кино").text)
        self.assertEqual(u"Театры", self.find_element_by_link_text(u"Театры").text)
        self.assertEqual(u"Концерты", self.find_element_by_link_text(u"Концерты").text)
        self.assertEqual(u"Вечеринки", self.find_element_by_link_text(u"Вечеринки").text)
        self.assertEqual(u"Выставки", self.find_element_by_link_text(u"Выставки").text)
        self.assertEqual(u"Цирк", self.find_element_by_link_text(u"Цирк").text)
        self.find_element_by_link_text(u"Полная версия").click()


class RegisterUser(BaseTestCase):
    def test_register_user(self):
        self.go_to(self.base_url + "/")
        self.find_element_by_link_text(u"Регистрация").click()
        self.input("FirstName", "SomeName")
        self.find_element_by_id("notMailGogle").click()
        self.find_element_by_xpath("//table[@id='tblFirstStep']/tbody/tr/td/label[2]").click()
        self.input("SecondName", "SomeSecondName")
        self.input("Username", "somemail@selenium.org")
        self.input("Password1", "somepassword2015")
        self.input("Password2", "somepassword2015")
        self.select_element("_3_1", u"1")
        self.select_element("_3_2", u"января")
        self.select_element("_3_3", "1992")
        self.find_element_by_id("msex").click()
        self.input("city_div0", "SomeCity")
        self.input("Answer", "SomeSurname2")
        self.input("ForgotPasswordPhone", "+375291234567")
        self.find_element_by_id("_14").click()
        self.find_element_by_id("reg_btn").click()
        self.find_element_by_id("city_div0").clear()
        self.input("city_div0", "")
        self.assertEqual(u"Не введено слово на картинке", self.find_element_by_id("idCodeMessage").text)


if __name__ == "__main__":
    unittest.main()
