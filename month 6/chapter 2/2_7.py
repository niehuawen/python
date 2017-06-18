#!/usr/bin/env python
# -- coding:utf-8 --
# while和for接收字符串并逐字符显示

while True:
    rev_str = raw_input("please input a string:")
    rev_str_length = len(rev_str)
    index = 0
    while index < rev_str_length:
        print(rev_str[index]),
        index += 1
    print("")

    for char in rev_str:
        print(char),
    print("")

    Qflag = raw_input("Do you want to continue？(Y) to Continue,(N) to Quit!")
    if Qflag in ("N","n","no","NO"):
        break
