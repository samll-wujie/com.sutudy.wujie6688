#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/25 19:02
# @Author  : wujie
'''
a = ['name'， "age"]
b = ['juran'， 18]
将上面两个列表   处理成 下面的形式
{"name" ：'juran', 'age' : 18}
'''

a = ['name', "age"]
b = ['juran', 18]
c = dict(zip(a, b))

print(c)

# 生成字典的方法
# 空字典
dic1 = {}
print(type(dic1))# <class 'dict'>
# 赋值创建字典
dic2 = {"name": "jack", "age": 12, "height": 180}
print("dic2", dic2) #2 {'name': 'jack', 'age': 12, 'height': 180}
# 关键字参数生成字典, 要有关键字才行
dic3 = dict(name="jack", age=12, height=180, bbb=1)
print("dic3", dic3) # {'name': 'jack', 'age': 12, 'height': 180, 'bbb': 1}

dict1 = {i: i * 2 for i in range(10)}
print(dict1)
