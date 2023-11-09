#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/9 22:19
# @Author  : wujie
'''
移除列表中多个元素
[3,5,7,9,11,13]
移除 元素： [7,11]
返回 [3,5,9,13]
'''

li = [3, 5, 7, 9, 11, 13]
li2 = [7, 11]
# 方法一

# for i in li2:
#     li.remove(i)
# print(li)


# 方法二
for i in li:
    if i in li2:
        # li.remove(i)
        li.pop(li.index(i))
print(li)
