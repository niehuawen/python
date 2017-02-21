#!/usr/bin/env python
# -- coding:utf-8 --

import time

#返回
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

print(fibo1(5))
print(fibo2(5))

