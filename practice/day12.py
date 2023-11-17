#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/17 22:11
# @Author  : wujie


'''
a = [1, 2, 3, 4]  b = [5, 4, 2, 1, 6]
找出a b 列表中不同的元素
'''


a = [1, 2, 3, 4, 9]
b = [5, 4, 2, 1, 6]
print("相同的元素：", set(a) & set(b))
print("不同的元素：", set(a) ^ set(b))