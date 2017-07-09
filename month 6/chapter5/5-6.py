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
        # 方式一
        # number1 = enter()
        # op = raw_input("please input a ops (+-*/%**):").strip()
        # if op not in ("+","-","*","/","%","**"):
        #     print("op input error,please enter again.")
        #     continue
        # number2 = enter()

        #方式二
        info = raw_input("please input your express:").strip()
        infolist = info.split()
        try:
            n1 = infolist[0].strip()
            n2 = infolist[2].strip()
            if "." in n1:
                number1 = float(n1)
            else:
                number1 = int(n1)
            if "." in n2:
                number2 = float(n2)
            else:
                number2 = int(n2)
        except Exception as e:
            print(e)
            break
        op = infolist[1].strip()
        result = cal(number1,op,number2)
        print("%s %s %s = %s" % (number1,op,number2,result))

if __name__ == "__main__":
    main()