#!/usr/bin/env python
# -- coding:utf-8 --
# 输入1-100之间的数值，满足条件显示并退出，不满足重新输入

while True:
    try:
        rev_str = raw_input("please input a number:")
        if "." in rev_str:
            number = float(rev_str)
        else:
            number = int(rev_str)
        if number >= 1 and number <= 100:
            print("%s Successfully."% (number))
            break
        else:
            print("not meet condition,Failed.")
            continue
    except ValueError as e:
        print(e)

