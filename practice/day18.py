#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/23 21:19
# @Author  : wujie
'''
将字符串中  的电话号 脱敏 替换成 1*******
s = "hello world13912345678dd heljinn 17712345678"
'''

import re

s = "hello world13912345678dd heljinn 17712345678"

ret = r"1[356789]\d{9}"

new_s = re.sub(ret, "1****", s)
print(new_s)