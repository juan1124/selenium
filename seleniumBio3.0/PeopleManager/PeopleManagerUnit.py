# -*- coding:utf8 -*-
__author__ = 'zk'

import unittest
from PeopleManager.PeopleManagerOp import PersonManager
from conf import customizeconf
from driver import drivercreator
from PeopleManager import PeopleManagerconf as conf



class PeopleMnagerUnitC(unittest.TestCase):

    # 测试前准备
    def setUp(self):

        driver = drivercreator.create_driver(customizeconf.driver_type)
        self.driver=driver
        self.PersonManager=PersonManager(driver)

    # 测试人员添加
    def Test_AddPerson(self):
        #PersonManager.AddPerson(self)
        self.PersonManager.AddPerson()
        # 断言
        self.assertEquals(1,1)

    # 测试人员删除
    def Test_DeletePerson(self):
        # 删除前人员数
        before_count = self.driver.find_element_by_xpath(conf.div_PersonCount).text
        before_count = before_count[1:-3]

        self.PersonManager.DeletePerson()
        # 获取删除后人员记录
        after_count=self.driver.find_element_by_xpath(conf.div_PersonCount).text
        after_count=after_count[1:-3]
        self.assertEquals(int(before_count)-1,int(after_count))

    def Test_ImportPerson(self):
        self.PersonManager.ImportPerson()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    testunit=unittest.TestSuite() #定义一个单元测试容器
    testunit.addTest(PeopleMnagerUnitC("Test_AddPerson"))


