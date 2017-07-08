#!/usr/bin/env python
# -- coding:utf-8 --
#description: 判断是否为闰年

from cf import enter

if __name__ == "__main__":
    while True:
        number = enter()
        if isinstance(number,float):
            print("%s is a float number , please input a int number." % number)
            continue
        elif isinstance(number,int):
            if (number % 4 == 0 and number % 100 != 0) or (number % 400 == 0 ):
                print("%s is a leap year." % number)
            else:
                print("%s is not a leap year." % number)

