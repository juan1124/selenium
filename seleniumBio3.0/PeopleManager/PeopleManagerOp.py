__author__ = 'zk'


from driver import drivercreator
from conf import customizeconf
import time
from PeopleManager import PeopleManagerconf as conf
from Common.Login import Login
from PeopleManager import data



class PersonManager():
    def __init__(self, driver):
        self.driver = driver
        self.login=Login(driver)
        self.login.Login_person()
        # 人事界面
        self.driver.find_element_by_css_selector(conf.link_peoplemanager).click()

    def AddPerson(self):
        browser = self.driver
        # browser=drivercreator.create_driver(customizeconf.driver_type)

        # 点击新增
        time.sleep(3)
        browser.find_element_by_xpath(conf.div_Addpeople).click()  # 通过xpath查找控件
        # browser.find_element_by_css_selector(conf.img_AddPeople).click() #点击图标

        browser.implicitly_wait(30)
        # 填写人员信息
        browser.find_element_by_xpath(conf.input_Pin).send_keys(data.pin)
        browser.find_element_by_id('personOK').click()
        time.sleep(4)

        # 删除人员
    def DeletePerson(self):
        browser=self.driver
        # 进入人事界面
        # browser.find_element_by_css_selector(conf.link_peoplemanager).click()
        # 选中某个人员
        browser.find_element_by_xpath(conf.CheckBox_SelectPerson).click()

        # 点击删除按钮
        browser.find_element_by_xpath(conf.div_Deletepeople).click()

        # 点击确认按钮
        browser.find_element_by_xpath(conf.div_DeleteOK).click()

        time.sleep(3)

        # 点击刷新按钮
        browser.find_element_by_xpath(conf.div_Refresh).click()

    def ImportPerson(self):
        browser=self.driver
        # 点击导入
        time.sleep(3)
        browser.find_element_by_xpath(conf.div_ImportPeople).click()
        browser.implicitly_wait(10)
        # browser.find_element_by_xpath(conf.td_ImportTable).click()
        browser.find_element_by_id("file").send_keys(data.ImportPerson_url)
        time.sleep(5)
        browser.find_element_by_id("nextStepButton").click()
        time.sleep(3)
        browser.find_element_by_id("nextStepButton").click()
        time.sleep(4)
        browser.find_element_by_id("lastStep").click()
        time.sleep(4)
