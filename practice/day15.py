#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/20 20:51
# @Author  : wujie

'''
给定2个字符串S1 he s2
确定其中一个字符串的字符重新排列后  能否变成另一个字符串
输入 s1 = "abc"   s2 = "bca"  输出 true
输入 s1 = "abc"  s2 = "bad"  输出 false
'''


def judgeStr(s1, s2):
    # for i in range(0, len(s1)-1):
    #     if s1[i] in s2:
    #         return True
    #     else:
    #         return False

    # 排序
    new_s1 = sorted(s1)
    new_s2 = sorted(s2)
    if new_s1 == new_s2:
        return True
    else:
        return False


a = "abc"
b = "efg"
print(judgeStr(a, b))
