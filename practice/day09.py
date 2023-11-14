#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/14 21:17
# @Author  : wujie


'''
两个列表  a = [1, 2, 3, 3]  b = [2, 8, 6, 4, 2]
合并为c = [1,2, 2, 2, 3, 3, 4, 6, 8]
'''

a = [1, 2, 3, 3]
b = [2, 8, 6, 4, 2]
c = a + b
# sorted(c) #返回一个对参数c列表排序后列表对象，原是列表c 不会变化
c.sort() #不会返回对象，是将c列表改变内部顺序 顺序排列， print(c.sort()) 结果none
print(c)
