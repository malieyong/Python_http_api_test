# _*_coding:utf-8_*_
"""
@author:malieyong
@time:2018/12/18 18:58
"""

def dog(name,type):

    def tiao(dog):
        print('狗在跳',dog['name'])

    def jiao(dog):
        print("狗在叫")

    dog1 = {
        'name':name,
        'type':type,
        'tiao':tiao,
        'jiao':jiao,
    }
    return dog1
# d1 = dog('袁浩','张傲')
# print(d1['tiao'](d1))



class Chines:

    dang = "共产党"

    def tu_tan():
        print("随地吐痰")

    def cha_dui():
        print('插队')
#
# print(Chines().dang)
#
# print(Chines.__dict__)  #使用__dict__   查看类属性字典
#
# Chines.__dict__['tu_tan']()


import json

a = '{"mobilephone":18688773467, "pwd":"123456"}'
print(type(json.loads(a)))



# str_test = '{"status": 0, "code": "20111", "data": null, "msg": "用户名或密码错误"}'




