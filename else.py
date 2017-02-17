#!/usr/bin/env python
# -- coding:utf-8 --

#for或者while循环，正常时的else都可以被执行，通过break退出循环的else均不被执行。

#由于break跳出，for循环没有被正常执行完，所以for...else中的else没有被执行
for number in range(10):
    if number <= 5:
        print("number:%s" %(number))
    else:
        break
else:
    print("hello world!")

print("*" * 30)

#for循环正常跳出，for...else中的else也正常被执行
for number in range(10):
    print("number:%s" %(number))
else:
    print("hello world!")

print("*" * 30)

#while循环break退出，while...else中else不被执行
num = 0
while num < 10:
    if num < 5:
        print("num:%s" %(num))
        num += 1
    else:
        break
else:
    print("hello world!")

print("*" * 30)

#while循环正常退出，while...else中else被执行
num = 0
while num < 10:
    print("num:%s" %(num))
    num += 1
else:
    print("hello world!")