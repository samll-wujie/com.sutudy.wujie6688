#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/27 20:38
# @Author  : wujie

'''
按逗号分隔示例
输入   l = {1, 2, 3, 4, 5}
输出 字符串 "1,2,3,4,5"
'''

# 方法一
l = {1, 2, 3, 4, 5}
s = ""
for i in l:
    s += str(i) + ","

print(s[:9])
# 方法二
s1 = ",".join(str(n) for n in l)
print(s1)


