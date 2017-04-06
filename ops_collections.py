#!/usr/bin/env python
#--coding:utf-8--

from collections import namedtuple

#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
#定义点坐标
Point = namedtuple("Point",["x","y"])
p = Point(1,2)
print(p.x,p.y)
print(isinstance(p,Point))
print(isinstance(p,tuple))

#定义圆
Circle = namedtuple("Circle",["x","y","r"])
c = Circle(1,2,3)
print(c.x,c.y,c.r)

print("*"*50)

#双向列表
from collections import deque
q = deque(["a","b","c"])
q.append("x")
q.appendleft("y")
print(q)
q.pop()
print(q)
q.popleft()
print(q)

print("*"*50)

#带默认值字典
from collections import defaultdict
dd = defaultdict(lambda :0)
dd["key1"] = "abc"
print(dd["key1"])
print(dd["key2"])

#有序字典
from collections import OrderedDict
d = dict([("a",1),("b",2),("c",3)])
print(d)

od = OrderedDict([("b",1),("a",2),("c",3)])
print(od)

od = OrderedDict()
od["z"] = 1
od["y"] = 2
od["x"] = 3
print(od.keys())

#计数器
from collections import Counter
c = Counter()
for ch in "programming":
    c[ch] = c[ch] + 1
print(c)
print(isinstance(c,dict))