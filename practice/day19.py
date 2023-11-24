#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/24 20:57
# @Author  : wujie
'''
取出列表 li = [1, 2, 3, 1, 11, 22, 12, 15, 1, 4]
中最大的三个值
'''
li = [1, 2, 3, 1, 11, 22, 12, 15, 1, 4]
new_li = sorted(li, reverse=True)
print(new_li)
for i in range(0, 4):
    print(new_li[i])