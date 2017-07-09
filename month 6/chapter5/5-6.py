#!/usr/bin/env python
# -- coding:utf-8 --
# description : 运算

from cf import enter

def cal(num1,ops,num2):
    if ops == "+":
        result = num1 + num2
    elif ops == "-":
        result = num1 - num2
    elif ops == "*":
        result = num1 * num2
    elif ops == "/":
        result = num1 / num2
    elif ops == "%":
        result = num1 % num2
    elif ops == "**":
        result = num1 ** num2
    return result

    # if ops in "+-*/%":
    #     result = eval(num1 ops num2)

def main():
    while True:
        number1 = enter()
        op = raw_input("please input a ops (+-*/%**):").strip()
        if op not in ("+","-","*","/","%","**"):
            print("op input error,please enter again.")
            continue
        number2 = enter()
        result = cal(number1,op,number2)
        print("%s %s %s = %s" % (number1,op,number2,result))

if __name__ == "__main__":
    main()