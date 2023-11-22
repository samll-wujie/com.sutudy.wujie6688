#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/22 21:26
# @Author  : wujie


'''
判断一个数字是否是一个对称数组
a = [1, 2, 3, 4, 3, 2, 1]  True
b = [1, 2, 1, 2] False
'''

a = [1, 2, 3, 4, 3, 2, 1]
print(a==a[::-1])