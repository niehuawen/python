#!/usr/bin/env python
# -- coding:utf-8 --
# description:enumerate()自定义函数，实现enumerate()内置函数的功能。
# 输入可迭代对象，返回enumerate对象的位置，通过list转换为list对象

def enumerated(iterable,start=0):
    n = start
    for item in iterable:
        yield n,item
        n += 1

var = ("a","b","c")
L1 = list(enumerated(var))
L2 = list(enumerate(var))
L3 = enumerate(var)     #L3为enumerate对象的位置
print(L1)
print(L2)
print(L3)