#!/usr/bin/env python
# -- coding:utf-8 --

#模块导入返回别名的函数
def importas(modulename):
    osalias = __import__(modulename)
    return osalias

osalias = importas("os")
print(osalias.listdir(r"c:/"))