#!/usr/bin/env python
# -- coding:utf-8

from operator import add,sub,mul,div
from random  import randint,choice

ops = {"+":add,"-":sub,"*":mul,"/":div}
MAXTRIES = 2

def doprob():
    op = choice("+-*/")
    nums = [randint(1,10) for i in range(2)]
    nums.sort(reverse = True)
    ans = ops[op](*nums)
    pr = "%d %s %d = " % (nums[0],op,nums[1])
    oops = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print("correct")
                break
            if oops == MAXTRIES:
                print("answer\n%s%d" %(pr,ans))
                break
            else:
                oops += 1
        except (KeyboardInterrupt,EOFError,ValueError):
            print("invalid input...try again")

def main():
    while True:
        doprob()
        try:
            opt = raw_input("Again?[y]").lower()
            if opt and opt[0] == "n":
                break
        except (KeyboardInterrupt,EOFError):
            break

if __name__ == "__main__":
    main()
