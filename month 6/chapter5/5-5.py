#!/usr/bin/env python
# -- coding:utf-8 --
# description: 取余运算

from cf import enter
unit = [1,5,10,25]

if __name__ == "__main__":
    while True:
        number = enter()
        dn = dict.fromkeys(unit,0)
        if number > 1:
            print(number)
            continue
        else:
            number *= 100
            for key in sorted(dn,reverse=True):
                knum,number = divmod(number,key)
                dn[key] = knum
        for key in dn:
            print(key,":",dn[key])
        print("total number is %s" % sum(dn.itervalues()))


