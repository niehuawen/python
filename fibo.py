#!/usr/bin/env python
# -- coding:utf-8 --

import time

#x相当于控制递归层数，当x大于某个层级如40时，执行存在问题
def fibo1(x):
    if x == 0 or x == 1:
        return 1
    elif x >= 2:
        return fibo1(x-1) + fibo1(x-2)

def fibo2(x):
    fibo_list = []
    for i in range(x):
        if i == 0 or i == 1:
            fibo_list.append(1)
        else:
            fibo_list.append(fibo_list[i-1]+fibo_list[i-2])
    return(fibo_list)

#时间复杂度分析
if __name__ == "__main__":
    t1 = time.clock()
    result1 = fibo1(40)
    t2 = time.clock()
    t3 = time.clock()
    result2 = fibo2(10000)
    t4 = time.clock()
    print("fibo1(40) cost time:%s" %(t2-t1))
    print("fibo2(10000) cost time:%s" %(t4-t3))


