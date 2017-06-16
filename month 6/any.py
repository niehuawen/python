#!/usr/bin/env python
# -- coding:utf-8 --

#内置函数any（）实现，判断可迭代对象中任一元素为True则返回True

def any(iterable):
    for item in iterable:
        if item:
            print("item type: {0} item: {1}".format(type(item),item))
            return True
    return False

tuple1 = ("0",2,0,0)
tuple2 = (0,0,3,0)

print(any(tuple1))
print(any(tuple2))
