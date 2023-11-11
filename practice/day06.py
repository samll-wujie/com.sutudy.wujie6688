#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/11 21:50
# @Author  : wujie
'''
对列表中的中元素去重
 li =  [1, 2, 3, 1]
 去重后得到 [1, 2, 3]

'''

li = [1, 2, 3, 1]
li2 = []
# 方法1：   先用set()   利用集合中无重复的元素特点将列表强制转换为集合，后强制转换为list
# print(list(set(li)))
# 方法2
for i in li:
    if i not in li2:
        li2.append(i)

print(li2)