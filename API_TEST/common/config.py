# -*- coding: utf-8 -*-
"""
# @Author   : malieyong
# @Time     : 2018/12/21 0:36
# @Email    : 15680978629@163.com
# @function : 配置文件
"""

import configparser
from common.contants import GetPath


class Conf:

    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.getpath = GetPath()

    #获取配置文件内数据 并通过base文件内容判断调用哪一个配置环境
    def get_base_url(self,section,option):
        file_name_path = self.getpath.get_conf_path_base()
        self.conf.read(file_name_path,encoding='utf-8')
        if self.get_boolean('switch','button'):
            file_1 = self.getpath.get_conf_environment_1()
            self.conf.read(file_1,encoding='utf-8')
            return self.conf[section][option]
        else:
            file_1 = self.getpath.get_conf_environment_2()
            self.conf.read(file_1,encoding='utf-8')
            return self.conf[section][option]

    #返回bool类型
    def get_boolean(self,section,option):
        return self.conf.getboolean(section,option)

    #返回int类型
    def get_int(self,section,option):
        return self.conf.getint(section,option)

    #返回float类型
    def get_float(self,section,option):
        return self.conf.getfloat(section,option)




if __name__ == '__main__':
    print(Conf().get_base_url('mysql','port'))