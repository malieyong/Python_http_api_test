# -*- coding: utf-8 -*-
"""
# @Author   : malieyong
# @Time     : 2018/12/19 23:03
# @Email    : 15680978629@163.com
# @function : 获取基础路径
"""


import os

class GetPath:
    # 获取基础路径
    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # conf_base 路径
    def get_conf_path_base(self):
        return os.path.join(self.base_path,'conf','base.conf')

    def get_conf_environment_1(self):
        return os.path.join(self.base_path,'conf','environment_1.conf')
    def get_conf_environment_2(self):
        return os.path.join(self.base_path,'conf','environment_2.conf')

    # datas 路径
    def get_datas_path(self):
        return os.path.join(self.base_path,'datas','testdatas.xlsx')

    # logs_path 路径
    def get_logs_path(self):
        return os.path.join(self.base_path,'logs','api_logs.txt')

    # report_path 路径
    def get_report_path(self):
        return os.path.join(self.base_path,'reports')

    #testcase_path 路径
    def get_testcase_path(self):
        return os.path.join(self.base_path,'testcase')


if __name__ == '__main__':
    # a =GetPath().get_datas_path()
    # print(a)
    print(GetPath().__dict__)