# -*- coding:utf-8 -*-
__author__ = 'zk'


# css选择器控件
# 人事按钮
link_peoplemanager='a[href="pers_index.action"]'

# 人事新增
# img_AddPeople='img[src="/public/images/opToolbar/comm_add.png"]'
div_Addpeople='//div[@class="dhxtoolbar_float_left"]/div[2]'
input_Pin = '//input[@name="user.pin" and @maxlength="9"]'

# 人员界面勾选某行记录
# CheckBox_SelectPerson='//td/input[@class="checkClass" and @name="ids"][1]'
CheckBox_SelectPerson = '//input[@class="checkClass" and @name="ids"][1]'

# 人员列表删除按钮
div_Deletepeople = '//div[@class="dhxtoolbar_float_left"]/div[4]'

# 记录总数
# div_PersonCount='//div[@class="dhx_toolbar_text" and @style="display: none;"][last()]'
div_PersonCount = '//div[@class="dhx_toolbar_text"][last()-1]'
# 刷新按钮
div_Refresh = '//div[@class="dhxtoolbar_float_left"]/div[1]'


# 删除确认按钮
div_DeleteOK = '//div[@class="dhtmlx_popup_button" and @result="true"]/div'


# 导入
# img_AddPeople='img[src="/public/images/opToolbar/comm_add.png"]'
div_ImportPeople = '//div[@class="dhxtoolbar_float_left"]/div[last()-1]'

# 导入页面
td_ImportTable = '//table[@class="imp_table"]/td[last()]'


