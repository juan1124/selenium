# -*- coding:utf8  -*-

__author__ = 'zk'
import os
import time


#修改某文件夹下的文件名
def change_name(path):
    global i
    if os.path.isfile(path):
        file_path=os.path.split(path)#分割出目录和文件
        print(file_path)
        lists=file_path[1].split('.')
        file_ext=lists[-1]
        # print(lists[1])
        txt_ext=['txt','html']
        if file_ext in txt_ext:
            os.rename(path,file_path[0]+'/'+lists[0]+'修改.'+file_ext)
            i+=1
    elif os.path.isdir(path):
        for x in os.listdir(path):
            # print(x)
            change_name(os.path.join(path,x))

def filename(path):
    for x in os.listdir(path):
        print(x)

path='D:\脚本\BioSecurity\ReuseableActions\platform'
filename(path)


