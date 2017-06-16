#!/usr/bin/env python
# -- coding:utf-8 --
# description: isinstance()判断对象实例是否属于某类型
# issubclass() 判断某类型是否属于另一个类型的子类

a = 1
b = "ab"
print(isinstance(a,int))
print(isinstance(a,float))
print(isinstance(b,str))
print(isinstance(b,list))

print(issubclass(bool,(int,str)))


