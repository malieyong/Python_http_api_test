# -*- coding: utf-8 -*-
"""
# @Author   : malieyong
# @Time     : 2018/12/20 20:49
# @Email    : 15680978629@163.com
# @function : 主逻辑
"""
from common import request
from common.do_excel import Do_Excel
from common.contants import GetPath
import json


class Runner:

    def __init__(self,sheet_cases):
        self.do_excel = Do_Excel(GetPath().get_datas_path())
        self.sheet_names = self.do_excel.get_all_sheet_names()  # 获取所有表单名字
        self.sheet_cases = sheet_cases        #指定需要执行的模块，可通过配置项进行修改

    #获取需要执行表单数据
    def get_execl_datas(self):
        #便利表单
        for sheet_name in self.sheet_names:
            # 确认需要执行的表单
            if sheet_name in self.sheet_cases:
                #返回表单数据->列表对象，以及表单名->字符串
                return self.do_excel.get_cases(sheet_name),sheet_name



if __name__ == '__main__':
    print(Runner('login').runner())
    # print(Runner.do_excel)
