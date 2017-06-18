#!/usr/bin/env python
# -- coding:utf-8 --
# 用户输入数据、菜单显示选择、求和、求均值、退出登录操作

def input_num():
    user_number = []
    while True:
        try:
            rev_str = raw_input("please input number('q'or 'Q' Exit):")
            if "." in rev_str:
                item = float(rev_str)
            else:
                item = int(rev_str)
            user_number.append(item)
        except ValueError as e:
            if rev_str in ("q", "Q", "quit", "exit"):
                break
            print(e)
    return(user_number)

def sum_num(num):
    total = sum(num)
    return(total)

def avg_num(num):
    #num_number为num的元素个数
    num_number = len(num)
    total = sum_num(num)
    avg = float(total) / num_number
    return(avg)

if __name__ == "__main__":
        prompt = """
            1). sum of number
            2). average of number
            X). quit
        """
        user_input_number = input_num()
        while True:
            print(prompt)
            choice = raw_input("please input your choice:")
            if choice not in ("1","2","X"):
                continue
            elif choice == "1":
                print sum_num(user_input_number)
            elif choice == "2":
                print avg_num(user_input_number)
            else:
                break