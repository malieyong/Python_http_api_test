# _*_coding:utf-8_*_
"""
@author:malieyong
@time:2018/12/17 1:49
"""

from ddt import ddt,data
import unittest
from common.main import Runner

datas,sheet_name = Runner().get_execl_datas()

@ddt
class ApiTest(unittest.TestCase):

    def setUp(self):
        print('22222222222')

    @data(*datas)
    def test_login(self,i):
        print("",i.url)







