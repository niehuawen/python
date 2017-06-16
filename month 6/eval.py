#!/usr/bin/env python
# -- coding:utf-8 --
# description: eval()函数功能实现字符串执行
# 输入参数：表达式字符串
# 返回值：计算后的值,可以为数值、字符串，也可以为布尔型，也可以为其他等

a = 100
b = "abc"
c = "def"
d = [1,2,3]
e = [4,5,6]
print(eval('a+10'))
print(eval('a-10'))
print(eval('a*10'))
print(eval('a/10'))
print(eval('a > 10'))
print(eval('a == 10'))
print(eval('a != 10'))
print(eval('a < 10'))
print(eval('b+c'))
print(eval('d + e'))
