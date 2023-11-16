#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/16 22:23
# @Author  : wujie
'''
输入一串带有空格的字符串，求出字符串的隔空后面的字符串的长度
'hello world'   返回5
'''

aStr = input("请输入一个带有空格的字符串：")
word = aStr.split(" ")
print(len(word[-1]))
