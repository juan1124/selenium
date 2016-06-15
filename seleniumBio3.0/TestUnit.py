# -*- coding:utf8 -*-

__author__ = 'zk'
import unittest
from PeopleManager.PeopleManagerUnit import PeopleMnagerUnitC
import xlrd
import os
import HTMLTestRunner
from PeopleManager import PeopleManagerUnit
import PeopleManager



if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    file_name='E:\\result.html'
    fp=open(file_name,'wb')
    #print(getattr(PeopleMnagerUnit,'PeopleMnagerUnit'))
    #print(getattr(PeopleManagerUnit,'Test_AddPerson'))
    #test_suite.addTests(PeopleMnagerUnitC('Test_AddPerson'))
    #打开excel
    case_file='E:\郑娟娟\SeleniumZKBio3.0\Testcase.xls'
    data=xlrd.open_workbook(case_file)
    table=data.sheet_by_name('TestCase')
    nrows=table.nrows
    ncols=table.ncols
    teseCases = []
    for i in range(1,nrows):
        if(table.cell(i,2).value==1):
            #teseCases=teseCases+'-'+table.cell(i,1).value
            teseCases.append(table.cell(i, 1).value)

   # print(teseCases)

    test_suite = unittest.TestLoader().loadTestsFromNames(teseCases)
    # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='人事模块', description='增删改查')
    runner.run(test_suite)  # 自动进行测试



