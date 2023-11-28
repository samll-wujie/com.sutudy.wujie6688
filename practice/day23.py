#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/28 22:07
# @Author  : wujie

'''
给出一个加密方式，对输入的字符串
其中从a-z，A-Z的字母用后面的一个字母代替输出，z和Z 用a和A替代
特殊的符号不变
比如  输入： hello world，python！
输出：Ifmm xpsme，qztipo！
'''

import re

password = input("请输入您的秘密：")
new_passworld = ""

for i in password:
    num = ord(i)
    if (97 <= num < 122) or (65 <= num < 90):
        pdw = chr(num + 1)
        new_passworld += pdw
    elif num == 122:
        pwd = chr(90)
        new_passworld += pwd
    elif num == 65:
        pwd = chr(97)
        new_passworld += pwd
    else:
        new_passworld += i
print(new_passworld)
