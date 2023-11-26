#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/26 18:22
# @Author  : wujie


'''
输入一行字符分别统计出其中英文字母、空格、数字
'''
import re

s = input("请输入一串字符：")
strCount = 0
spcaeCount = 0
numCount = 0
for i in s:
    if i.isalpha():
        strCount += 1
    elif i.isspace():
        spcaeCount += 1
    elif i.isdigit():
        numCount += 1
print("英文：%d，空格：%d，数字：%d" % (strCount, spcaeCount, numCount))
