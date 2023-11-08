#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/7 21:55
# @Author  : wujie

'''
输入半径，求出圆的面积
'''
import math

radius = float(input("请输入圆的半径："))

area = math.pi*radius*radius

print(area)