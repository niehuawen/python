#!/usr/bin/env python
# -- coding:utf-8 --
# description: 过滤符合条件的元素
# 参数：函数名和可迭代对象
# 返回：符合条件的元素的列表

def filter35(x):
    if x % 3 == 0 or x % 5 == 0:
        return x

print(filter(filter35,range(90)))


