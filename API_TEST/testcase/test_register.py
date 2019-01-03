# -*- coding: utf-8 -*-
"""
# @Author   : malieyong
# @Time     : 2018/12/26 22:37
# @Email    : 15680978629@163.com
# @function : 注册模块
"""

import json
import unittest
from ddt import ddt, data
from common import request
from common.main import Runner
from common.loggers import Log
from common.do_excel import Do_Excel
from common.contants import GetPath

datas, sheet_name = Runner('register').get_execl_datas()
get_do_excel = Do_Excel(GetPath().get_datas_path())

@ddt
class TestRegister(unittest.TestCase):

    def setUp(self):
        pass

    @data(*datas)
    def test_register(self, item):
        python_dict = json.loads(item.request_data)
        try:
            # 调用url进行拼接
            item_url = get_do_excel.join_url(sheet_url=item.url)
            res = request.Request(url=item_url, method=item.method, data=python_dict)
            expect = json.loads(item.expect)['code']    #获取期望值code
            practical = res.get_josn()['code']          #获取实际值code
            try:
                self.assertEqual(expect, practical)
                # 回写测试结果成功
                get_do_excel.write_practical_by_case_id(sheet_name=sheet_name,case_id=item.id,practical=res.get_text(),
                                                        result='succeed')
                # 增加日志输出
                Log().out_debug('pass', item.api_describe, res.get_josn())
            except:
                # 回写测试结果失败
                get_do_excel.write_practical_by_case_id(sheet_name=sheet_name,case_id=item.id,practical=res.get_text(),
                                                        result='fail')
                # 增加日志输出
                Log().out_debug('file', item.api_describe, res.get_josn())

        except SyntaxError as e:
            print('{0}功能,第{1}用例执行失败,失败用例描述名称{2},参数未赋值'.format(item.api, item.id, item.api_describe))
            raise e

    #关闭数据库连接
    def tearDown(self):
        pass