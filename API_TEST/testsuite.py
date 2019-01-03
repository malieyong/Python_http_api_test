# -*- coding: utf-8 -*-
"""
# @Author   : malieyong
# @Time     : 2018/12/23 21:51
# @Email    : 15680978629@163.com
# @function : 测试集->收集->执行
"""
import unittest
# from testcase.test_login import TestLogin
from testcase.test_recharge import TestRecharge
# from testcase.test_register import TestRegister
from BeautifulReport import BeautifulReport
from common.contants import GetPath


#为测试集开辟存储空间
test_suite = unittest.TestSuite()

#加载测试用例
test_loader = unittest.TestLoader()

# test_suite.addTest(test_loader.loadTestsFromTestCase(TestRegister))   # 注册
# test_suite.addTest(test_loader.loadTestsFromTestCase(TestLogin))      # 登录
test_suite.addTest(test_loader.loadTestsFromTestCase(TestRecharge))     # 充值


# runner = unittest.TextTestRunner()
# runner.run(test_suite)

#执行测试用例，并输出测试报告
BeautifulReport(test_suite).report(description='API接口测试', filename='API测试报告', log_path=GetPath().get_report_path())