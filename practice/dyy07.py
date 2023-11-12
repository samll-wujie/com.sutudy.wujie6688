#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/12 22:36
# @Author  : wujie


'''
求数字的阶成
如  5*4*3*2*1=
'''

def demo(m):
    n =1
    for i in range(1, m):
        n =i * n
        # print( n)
    return n


print(demo(4))
