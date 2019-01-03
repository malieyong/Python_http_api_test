# -*- coding: utf-8 -*-
"""
# @Author   : malieyong
# @Time     : 2018/12/24 0:35
# @Email    : 15680978629@163.com
# @function : 日志打印
"""

import logging
from common.contants import GetPath

class Log:

    def __init__(self):

        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s- %(message)s')

        #设置日志收集器
        self.my_logger = logging.getLogger('十月')
        self.my_logger.setLevel("DEBUG")

        #设置输出日志
        self.fh = logging.FileHandler(GetPath().get_logs_path(),encoding='utf-8')
        self.fh.setLevel('DEBUG')
        self.fh.setFormatter(self.formatter)

        #对接
        self.my_logger.addHandler(self.fh)


    #设置输出DEBUG级别日志
    def out_debug(self,*args):
        self.my_logger.debug(args)
        self.my_logger.removeHandler(self.fh)

    #设置输出INFO级别日志
    def out_info(self,*args):
        self.my_logger.info(args)
        self.my_logger.removeHandler(self.fh)



if __name__ == '__main__':
    # print(Log().formatter.__dict__['_fmt'])
    a =2
    b=3
    Log().out_debug("qqqqqqqqq",a,b)

