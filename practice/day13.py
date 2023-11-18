#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/18 22:58
# @Author  : wujie
'''
猜数字游戏，小了输出小了，大了输出大了，直到才对
'''
import random

while (True):
    answer = random.randint(1, 10)
    inInt = int(input("请输入一个数字："))
    if inInt > answer:
        print("猜大了")
    elif inInt < answer:
        print("猜小了")
    else:
        print("恭喜，猜对了")
        break

