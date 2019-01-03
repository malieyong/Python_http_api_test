# _*_coding:utf-8_*_
"""
@author:malieyong
@time:2018/12/18 23:52
"""

import requests


class Request:

    def __init__(self,url,method,data=None,cookies=None,headers=None):
        try:
            if method=='get':
                self.resp = requests.get(url=url,params=data,cookies=cookies,headers=headers)
            elif method=='post':
                self.resp = requests.post(url=url,data=data,cookies=cookies,headers=headers)
            elif method=='delete':
                self.resp = requests.delete(url=url, params=data, cookies=cookies, headers=headers)
        except Exception as e:
            raise e

    #获取响应码并返回
    def get_status_code(self):
        return self.resp.status_code

    # 获取响应数据-并返回text格式
    def get_text(self):
        return self.resp.text

    # 获取响应数据-并返回josn格式
    def get_josn(self):
        return self.resp.json()

    # 获取cookies并返回
    def get_cookies(self):
        return self.resp.cookies

    # 获取请求头并返回
    def get_header(self):
        return self.resp.headers