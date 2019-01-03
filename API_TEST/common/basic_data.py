# -*- coding: utf-8 -*-
"""
# @Author   : malieyong
# @Time     : 2019/1/1 22:52
# @Email    : 15680978629@163.com
# @function : 基础数据
"""

#通过反射进行数据添加和维护
#1、cookies
class Context:

    # cookies = None
    # header = None
    pass


if __name__ == '__main__':
    for i in range(3):
        if hasattr(Context, 'cookies'):
            cookies = getattr(Context, 'cookies')
        else:
            cookies = None
        setattr(Context,'cookies','222')
        print(cookies)
