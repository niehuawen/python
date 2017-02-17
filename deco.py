#!/usr/bin/env python
# -- coding:utf-8 --

from time import ctime,sleep

#装饰器本质也为函数
def tsfunc(func):
    #wrapperFunc函数也为称为闭包，因为调用外部函数的对象func
    def wrapperFunc():
        print("[%s] %s() called" % (ctime(),func.__name__))
        return func()
    #wrapperFunc而不是wrapperFunc()
    return wrapperFunc


@tsfunc
def foo():
    pass

#执行等同于tsfunc(func)(foo())
foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()
