__author__ = 'Administrator'
import time
from selenium import webdriver
from conf import customizeconf as cu
from selenium.webdriver.common import keys

from driver import drivercreator

from AuthManager import Authconf as conf
from Common.Login import Login

class AuthManager ( ):

    # 初始化
    def __init__(self):
       driver = drivercreator.create_driver(cu.driver_type)
       self.driver = driver

    def out_online(self):
        browser = self.driver
        login = Login(browser)
        login.Login_person()
        # 打开许可页面
        browser.implicitly_wait(3)
        browser.find_element_by_id("base_system_about").click()
        # 点击在线激活
        time.sleep(6)
        browser.find_element_by_link_text("Online Activation").click()
        # self.driver.quit()

    def loadsn(self):
        #driver = drivercreator.create_driver(cu.driver_type)
        driver = self.driver
        driver.get(cu.auth_url)
        driver.find_element_by_link_text("继续浏览此网站(不推荐)。").click()
        driver.implicitly_wait(3)
        driver.find_element_by_id("langSelect").click()
        time.sleep(3)
        driver.find_element_by_id("system.language.chinese").click()

        driver.find_element_by_name("userName").send_keys(cu.out_username)
        driver.find_element_by_name("password").send_keys(cu.out_password)
        driver.find_element_by_xpath(conf.auth_sumbit).click()

        # driver.implicitly_wait(5)
        # driver.find_element_by_id("addSN").click()
        # driver.find_element_by_id("select").click()
        # time.sleep(3)
        # driver.find_element_by_xpath(conf.auth_select).click()
        # time.sleep(3)
        # driver.find_element_by_id("limitDevice11").send_keys("5")
        # driver.find_element_by_id("pushAccessControl").click()
        # driver.find_element_by_id("limitDevice18").send_keys("10")
        #
        # companyname="int-"+time.strftime('%y-%m-%d-%H-%M-%S', time.localtime())
        # driver.find_element_by_xpath(conf.auth_companyname).send_keys(companyname)
        # driver.find_element_by_xpath(conf.addsn_sumbit).click()
        # time.sleep(3)
        # alert_window = driver.switch_to_alert()
        # print()
        # alert_window.accept()
        # driver.find_element_by_id("companyName").send_keys(companyname)

        # driver.find_element_by_xpath(conf.auth_search).click()
        tables = driver.find_elements_by_css_selector(conf.auth_table)
        tables[1].find_element_by_link_text("查看许可列表").click()
        time.sleep(2)
        now_handle = driver.current_window_handle  # 获取当前窗口句柄
        print(now_handle)

        driver.find_element_by_css_selector(conf.auth_downSN).click()

        # driver.find_element_by_css_selector(conf.auth_return).click()
        driver.switch_to_window(driver.window_handles[-1]).find_element_by_css_selector(conf.auth_downSN).send_keys(keys.Keys.ALT, 's')

        now_handle = driver.current_window_handle  # 获取当前窗口句柄
        print(now_handle)



if __name__ == '__main__':
    # driver = drivercreator.create_driver(customizeconf.driver_type)
    a = AuthManager()
    a.loadsn()

