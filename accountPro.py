#!/usr/bin/env python
# -- coding:utf-8 --

import pickle
import os

"""pickle基础操作
fdata = open("data.txt","rb")
userdata = pickle.load(fdata)
fdata.close()

fdata = file("data.txt","wb")
pickle.dump(userdata,fdata)
fdata.close()
"""

def pickle_load(filename):
    with open(filename,"rb") as input_file:
        try:
            return pickle.load(input_file)
        except:
            return None

def pickle_dump(context,filename):
    with open(filename,"wb") as output_file:
        pickle.dump(context,output_file)

"""
userdata = {"username":"niehuawen","password":"2017!@#",1:{"Smoney":10000,"lend":0}}
pickle_dump(userdata,"data.txt")
p = pickle_load("data.txt")
for key in p:
    print(key,p[key])
"""

#显示账户余额
def show_account(filename,type=1):
    try:
        userdata = pickle_load(filename)
    except:
        print("file %s not existed!" %(filename))
    if type not in range(1,5):
        print("account type error!")
    else:
        for key in userdata[type]:
            print("%s:%s" %(key,userdata[type][key]))

#取钱函数
def deposit_money(filename):
    #用户数据字典
    userdata = pickle_load(filename)
    #取钱金额
    d_money = int(input("how much you want to deposit ?").strip())
    #用户初始金额
    init_money = userdata[1]["Smoney"]
    #取钱后余额
    userdata[1]["Smoney"] = init_money - d_money
    #是否确定取钱操作
    flag = input("Do you want to continue this deposit ops ? (y stand for continue)")
    if flag == "yes" or flag == "y":
        print("Deposit money %s success!" % (d_money))
    #取消取钱操作时确定退回被减去的金额，防止多次取消操作导致大于原有初始金额
    elif init_money == userdata[1]["Smoney"] + d_money:
        userdata[1]["Smoney"] = userdata[1]["Smoney"] + d_money
    #将数据写会至原文件
    pickle_dump(userdata,filename)

#存钱函数
def withDraw(filename):
    # 用户数据字典
    userdata = pickle_load(filename)
    # 存钱金额
    w_money = int(input("how much you want to withDraw ?").strip())
    # 用户初始金额
    init_money = userdata[1]["Smoney"]
    # 存钱后余额
    userdata[1]["Smoney"] = init_money + w_money
    # 是否确定存钱操作
    flag = input("Do you want to continue this withdraw ops ? (y stand for continue)")
    if flag == "yes" or flag == "y":
        print("Withdraw money %s success!" % (w_money))
    # 取消存钱操作时确定退回被存进的金额，防止多次取消操作导致少于原有初始金额
    elif init_money == userdata[1]["Smoney"] - w_money:
        userdata[1]["Smoney"] = userdata[1]["Smoney"] - w_money
    # 将数据写会至原文件
    pickle_dump(userdata, filename)

def lendBorrow(filename):
    # 用户数据字典
    userdata = pickle_load(filename)
    # 借出金额
    l_money = int(input("how much you want to lendBorrow ?").strip())
    # 用户初始金额
    init_money = userdata[1]["Smoney"]
    init_lend = userdata[1]["lend"]
    if l_money <= init_money:
        # 借钱后余额
        userdata[1]["Smoney"] = init_money - l_money
        userdata[1]["lend"] = init_lend + l_money
        # 是否确定借钱操作
        flag = input("Do you want to continue this lendout ops ? (y stand for continue)")
        if flag == "yes" or flag == "y":
            print("Lendout money %s success!" % (l_money))
        # 取消存钱操作时确定退回被存进的金额，防止多次取消操作导致少于原有初始金额
        elif init_money == userdata[1]["Smoney"] + l_money and init_lend == userdata[1]["lend"] - l_money :
            userdata[1]["Smoney"] = userdata[1]["Smoney"] + l_money
            userdata[1]["lend"] = userdata[1]["lend"] - l_money
    else:
        print("you can lendout should not more %s money!" %(init_money))
    # 将数据写会至原文件
    pickle_dump(userdata, filename)

def SaOpsMenu():
    prompt = """
    (S)how Storage account 查看
    (D)eposit money 取钱
    (W)ithdraw 存钱
    (L)end Borrow 借钱
    (Q)uit     退出
    Enter Char [S D W L B] Choice:"""
    while True:
        try:
            choice = input(prompt).strip().lower()
        except:
            choice = "q"
        if choice not in "sdwlbq":
            choice == "q"
        elif choice == "s":
            #fname = input("datafile:").strip()
            fname = "data.txt"
            if os.path.isfile(fname):
                show_account(fname)
        elif choice == "d":
            fname = "data.txt"
            deposit_money(fname)
        elif choice == "w":
            fname = "data.txt"
            withDraw(fname)
        elif choice == "l":
            fname = "data.txt"
            lendBorrow(fname)
        elif choice == "q":
            break

def CaOpsMenu():
    print("CaOpsMenu")

def FaOpsMenu():
    print("FaOpsMenu")

def DaOpsMenu():
    print("DaOpsMenu")

def showMenu():
    prompt = """
    1.Storage account
    2.Checking account
    3.Financial account
    4.Deposit Account
    5.Quit
    Enter Number 1-5 Choice:"""
    while True:
        try:
            choice = int(input(prompt).strip())
        except:
            choice = 5
        if choice not in range(1,6):
            choice = 5
        elif choice == 1:
            SaOpsMenu()
        elif choice == 2:
            CaOpsMenu()
        elif choice == 3:
            FaOpsMenu()
        elif choice == 4:
            DaOpsMenu()
        elif choice == 5:
            break

if __name__ == "__main__":
    showMenu()