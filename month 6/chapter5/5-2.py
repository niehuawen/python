#!/usr/bin/env python
# -- coding:utf-8 --
#
import string

# st 等价于 "0123456789."
st = string.digits + "."

# 乘法运算
def involution(num1,num2):
    return(num1*num2)

#用户输入数字，并判断字符串为浮点数字符串还是整数字符串
def enter():
    while True:
        rev_str = raw_input("please input a number:").strip()
        for ch in rev_str:
            if ch not in st:
                print("invalid number ,please input again.")
                break
        else:
            if "." in rev_str:
                return(float(rev_str))
            else:
                return(int(rev_str))

if __name__ == "__main__":
    v1 = enter()
    v2 = enter()
    result = involution(v1,v2)
    print("%s * %s = %s " % (v1,v2,result))