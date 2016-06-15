#encoding=utf-8
__author__ = 'zk'


from testlink import *
import html.parser as h

import urllib.request
import urllib.parse
import urllib.response
import testlink.testlinkapi
import os
import shutil
import time
import sys,string
import stat
from selenium import webdriver
from driver import drivercreator
from conf import customizeconf

class ce():

    def updateResult(self):
        pass
        urlStr = "http://192.168.1.68:8010/testlink/lib/api/xmlrpc.php"
        devKey = "e009be14c15a151be8b23f5a961510c3"
        tlc = TestlinkAPIClient(urlStr, devKey)
        plan = tlc.getTestPlanByName("ZKBioSecurity3.0", "测试")
        build = tlc.getBuildsForTestPlan(plan[0]["id"])
        tlc.reportTCResult(1827, plan[0]["id"], build[0]["name"], "p", "备注")

    def html(self):

        file_name = 'E:\\result.html'
        # fp = open(file_name, 'r')
        # os.system(r"E:\\result.html")
        driver = drivercreator.create_driver(customizeconf.driver_type)
        driver.get(file_name)
        driver.find_element_by_link_text("Detail").click()
        a = '//table[@id="result_table"]//tr[@class=""]'
        sea = driver.find_elements_by_xpath(a)
        num = sea.__len__()
        dic = {'a': 'b'}
        dic.clear()
        for i in range(1, num+1):
            key = a + '['+str(i)+']//td[1]'
            value = a + '['+str(i)+']//td[2]'
            dic[driver.find_element_by_xpath(key).text] = driver.find_element_by_xpath(value).text



if __name__ == '__main__':
    p = ce()
    p.html()




#重要文件创建备份的程序

# sourcepath=[r'D:/a/a.txt']
# targetpath=r'D:/new'
# targetfile=targetpath+time.strftime('%Y%m%d%H%M%S')
#
# os.mkdir(targetfile)
# for path in sourcepath:
#     #os.chmod(targetfile, stat.S_IWOTH)
#     shutil.copyfile(path,targetfile)






