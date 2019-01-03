# -*- coding: utf-8 -*-
"""
# @Author   : malieyong
# @Time     : 2018/12/23 20:07
# @Email    : 15680978629@163.com
# @function :
"""

import re
import json
from testcase.mysql_datas import SelectPhone
from common.main import Runner

#----------好的----------
# keys = "{\"mobilephone\":\"${222}\",\"pwd\":123456}"  # 这段是你要匹配的文本
# mysql_phone = str(SelectPhone().select_connect())
# replace_start = re.compile("\$\{\d+\}")
# replace_end = replace_start.sub(mysql_phone,keys)
# print(replace_end)




datas, sheet_name = Runner().get_execl_datas()
for item in datas:
    sheet_request_data = item.request_data
    mysql_phone = str(SelectPhone().select_connect())
    replace_start = re.compile("\$\{\d+\}")
    replace_end = replace_start.sub(mysql_phone,sheet_request_data)
    print(replace_end)
