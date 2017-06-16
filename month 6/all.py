#!/usr/bin/env python
# -- coding:utf-8 --

#内置函数all（）实现，判断可迭代对象中任意元素都为True则返回True

def all(iterable):
    for item in iterable:
        if not item:
            print("the item is {0}".format(item))
            return False
    return True

list1 = [0,'a','b','cd']
list2 = {"a":1,"b":2,"c":3,"":1}

print(all(list1))
print(all(list2))