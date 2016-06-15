# -*- coding:utf8 -*-

__author__ = 'zk'

from driver import drivercreator
from conf import customizeconf
import time

#登录

class Login():
    def __init__(self, driver):
        self.driver = driver

    def Login_person(self):
        # browser=drivercreator.create_driver(customizeconf.driver_type)
        browser = self.driver
        browser.get(customizeconf.base_url)
        browser.find_element_by_id('usernameTip').click()
        browser.find_element_by_id('username').send_keys('admin')
        browser.find_element_by_id('passwordTip').click()
        browser.find_element_by_id('password').send_keys('admin')
        browser.find_element_by_class_name('but_login').click()
        time.sleep(2)
