#!/usr/bin/env python=3.8.1
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 17:55
# @Author  : wujie

'''
对学生成绩（scores）列表排序
student = [{"id": 100, "name": "xxx", "scores": 90}, {"id": 101, "name": "yyy", "scores": 80},
            {"id": 102, "name": "zzz", "scores": 70}]
'''

student = [{"id": 100, "name": "xxx", "scores": 79}, {"id": 101, "name": "yyy", "scores": 89},
           {"id": 102, "name": "zzz", "scores": 69}]

for i in student:
    print(i["scores"])

stu_sort = sorted(student, key=lambda i: i["scores"], reverse=False)
print(stu_sort)
