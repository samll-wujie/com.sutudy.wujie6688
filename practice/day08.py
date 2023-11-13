#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/13 20:01
# @Author  : wujie
'''
有四个数字 1， 2， 3， 4，
组成无重复的三位数多少个
'''

numList = []
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            num = i*100+j*10+k
            if num not in numList and j !=i and i != k and j !=k:
                numList.append(num)
print(len(numList))


