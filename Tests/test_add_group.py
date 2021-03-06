__author__ = "Artur"
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.Login(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="Training", header="Crom", footer="Gry"))
        self.return_to_group_list(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.Login(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="", header="", footer=""))
        self.return_to_group_list(wd)

    def return_to_group_list(self, wd):
        # return to group list
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        # open group page
        wd.find_element_by_link_text("groups").click()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill all group fields
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit groups page
        wd.find_element_by_name("submit").click()


    def Login(self, wd, username, password):
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
