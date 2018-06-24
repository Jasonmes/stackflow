#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

# 自定义异常处理
class CustomException(Exception):
    def __init__(self, info):
        self.info = info
    
    def __str__(self):
        return self.info

phone_num = input("请输入手机号：")

try:
    if len(phone_num) != 11:
        raise CustomException("手机号码位数不对")
    elif phone_num.isdecimal() == False:
        raise CustomException("手机号码不合法")
except CustomException as error:
    print(error)




