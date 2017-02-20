#!/usr/bin/env python
# -- coding:utf-8 --

import time

def func(x):
    for i in range(1,x):
        print("num:%d" %(i))
        time.sleep(1)

#函数时间性能测试
def testit(func1,x=5):
    t1 = time.clock()
    func1(x)
    t2 = time.clock()
    return(t2-t1)

timecost = testit(func,10)
print("time cost:%s" %(timecost))

timecost = testit(func)
print("time cost:%s" %(timecost))