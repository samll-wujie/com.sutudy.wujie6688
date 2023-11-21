#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/21 20:06
# @Author  : wujie
'''
# 给定一个字符串 将其中的空格替换为 “%20”
如 s = "we are happy."
输出 "we%20are%20happy."
'''


def replaceStr(s):
    new_s = s.replace(" ", "%20")
    return new_s


s = "we are happy."
print(replaceStr(s))
