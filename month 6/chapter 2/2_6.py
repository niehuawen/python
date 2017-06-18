#!/usr/bin/env python
# -- coding:utf-8 --
# 判断正负数

while True:
    try:
        rev_str = raw_input("please input a number:")
        number = float(rev_str)
        if number > 0:
            print("%s is a + number." % (number))
        elif number == 0:
            print("%s is zero" % (number))
        else:
            print("%s is - number." % (number))
    except ValueError as e:
        if rev_str in ("q", "Q", "quit", "Quit", "QUIT"):
            break
        print(e)




