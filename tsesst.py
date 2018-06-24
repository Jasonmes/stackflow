#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

# 异常处理
try:
    f = open("/Users/jason/Desktop/今日练习/search_index.json", "r")
    content = f.read()
    # print(content)
    f.close()
    # print(a)
except FileNotFoundError as error:
    print(error)
except NameError as error:
    print(error)
else:
    print("当try里面的代码没有出错时，就会执行else中的代码")
finally:
    print("不管try里面的代码有没有错，finally都会执行")