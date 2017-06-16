#!/usr/bin/env python
# -- coding:utf-8 --
# description:功能 使用bin()函数实现数字至数字的二进制字符串表现
# 输入：数字；返回输出：字符串

while True:
    try:
        num = int(raw_input("please input a number："))
        str = bin(num)
        print("binary of {0} is {1}".format(num,str))
    except ValueError,e:
        print(e.message)
    else:
        flag = raw_input("'y' to continue 'n' to quit:")
        if flag == 'n':
            break


