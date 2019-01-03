# -*- coding: utf-8 -*-
"""
# @Author   : malieyong
# @Time     : 2018/12/22 13:58
# @Email    : 15680978629@163.com
# @function : 查询手机号
"""
from common.config import Conf
import pymysql


mysql_select = "SELECT MobilePhone FROM future.member ORDER BY MobilePhone DESC"

class SelectPhone:
    def __init__(self):
        self.host = Conf().get_base_url('mysql','host')
        self.port = Conf().get_base_url('mysql','port')
        self.root = Conf().get_base_url('mysql','root')
        self.pwd = Conf().get_base_url('mysql','pwd')
        self.db = pymysql.connect(host=self.host, user=self.root, password=self.pwd, port=int(self.port),
                                  )   #建立连接
        self.cursor = self.db.cursor()  #建立游标


    #查询最大的手机号-并加1
    def select_connect(self):
        try:
            # 执行语句
            self.cursor.execute(query=mysql_select)
            # 手机号加1
            return int(self.cursor.fetchone()[0])+1
        # 事务回滚
        except Exception as e:
            print('Find an Error,now rollback!')
            self.db.rollback()
            raise e

    #关闭数据库连接
    def close_connect(self):
        self.db.close()

if __name__ == '__main__':
    # print(SelectPhone().select_connect())
    print(SelectPhone().a)

