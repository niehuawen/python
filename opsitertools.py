#!/usr/bin/env python
#--coding:utf-8--

#无限循环下去

import itertools
"""
natuals = itertools.count(1)
for n in natuals:
    print n
"""

#无限重复下去
"""
cs = itertools.cycle("ABC")
for c in cs:
    print c
"""

#输出"a" 10次
"""
ns = itertools.repeat("a",10)
for n in ns:
    print n
"""

#循环1-10
"""
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=10,natuals)
for n in ns:
    print n
"""

#输出A B C X Y Z
"""
for c in itertools.chain("ABC","XYZ"):
    print c
"""

#默认区分大小写
for key,group in itertools.groupby("AAAaBBBBcCCCCDdddd"):
    print(key,list(group))

print("*"*50)

for key,group in itertools.groupby("aAAAAbcccCCCdddddDDD",lambda c:c.upper()):
    print(key,list(group))