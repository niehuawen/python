#!/usr/bin/env python
# -- coding:utf-8 --
# 排序算法：由小至大，由大至小

def input_number():
    while True:
        try:
            istr = raw_input("enter a number:")
            if "." in istr:
                number = float(istr)
            else:
                number = int(istr)
            return number
        except ValueError as e:
            print(e)

# 由小至大输出
def small2large(num1,num2,num3):
    t = 0
    if num1 > num2:
        t = num1
        num1 = num2
        num2 = t
    if num1 > num3:
        t = num1
        num1 = num3
        num3 = t
    if num2 > num3:
        t = num2
        num2 = num3
        num3 = t
    return(num1,num2,num3)

# 由大至小输出
def large2small(num1,num2,num3):
    t = 0
    if num1 < num2:
        t = num1
        num1 = num2
        num2 = t
    if num1 < num3:
        t = num1
        num1 = num3
        num3 = t
    if num2 < num3:
        t = num2
        num2 = num3
        num3 = t
    return(num1,num2,num3)

if __name__ == "__main__":
    a = input_number()
    b = input_number()
    c = input_number()
    result1 = small2large(a,b,c)
    result2 = large2small(a,b,c)
    print(result1)
    print(result2)


