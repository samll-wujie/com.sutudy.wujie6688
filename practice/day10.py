#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/15 20:59
# @Author  : wujie
'''
[[1, 2, 3], [4, 5, 6], [7, 8, 9]] 一行代码展开列表得到
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

# 多行展示
# li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# newLi = []
# for i in li:
#     for j in i:
#         newLi.append(j)
#
# print(newLi)
# newLi = [j for i in li for j in i]
# 一行展示，列表推导式
print([j for i in [[1, 2, 3], [4, 5, 6], [7, 8, 9]] for j in i])


# extend() list.extend(sep)
alist = [1, 2, 3]
blist = [4, 5, 6]
print(alist.extend(blist)) # 返回None
print('列表加列表：', alist)  # 返回[1, 2, 3, 4, 5, 6]
cStr ='adb'
alist.extend(cStr)
print("列表加字符串：", alist)  # 列表加字符串： [1, 2, 3, 4, 5, 6, 'a', 'd', 'b']

dTuple = (11, 22)
alist.extend(dTuple)
print("列表加元组：", alist)  # 列表加元组： [1, 2, 3, 4, 5, 6, 'a', 'd', 'b', 11, 22]

eDict = {"k": "v", "kk": "vv"}
alist.extend(eDict)
print("列表加字典：", alist)   # 列表加字典： [1, 2, 3, 4, 5, 6, 'a', 'd', 'b', 11, 22, 'k', 'kk']

fSet = {111, 333, 222, 123}
alist.extend(fSet)
print("列表加集合：", alist)   # 列表加集合： [1, 2, 3, 4, 5, 6, 'a', 'd', 'b', 11, 22, 'k', 'kk', 123, 333, 222, 111]




