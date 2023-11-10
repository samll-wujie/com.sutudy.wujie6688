#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/10 22:45
# @Author  : wujie
'''
删除列表中重复的元素
去重后的元素相对位置保持不变
li = [2, 1, 3, 1, 2]
'''

li = [2, 1, 3, 1, 2, 5, 1, 3, 3, 4, 5]
# li = list(set(li))
print(li)   # [1, 2, 3]    位置变了

li2 = []

for i in li:
    if i not in li2:
        li2.append(i)

print(li2)




