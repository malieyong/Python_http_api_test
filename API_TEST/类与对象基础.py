# -*- coding: utf-8 -*-
"""
# @Author   : malieyong
# @Time     : 2018/12/26 0:02
# @Email    : 15680978629@163.com
# @function :
"""

class Login:

    url ='http://www'
    user = 1568097
    pwd = "qwerdf"


'''
你也可以使用以下函数的方式来访问属性：
getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) :             检查是否存在一个属性。
setattr(obj,name,value) :       设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) :            删除属性
'''
# print(getattr(Login,'url'))     #获取对象属性
# setattr(Login,'port','3306')    #增加对象属性
# print(getattr(Login,'port'))
# print(hasattr(Login,'port'))    #判断是否存在，返回布尔类型

