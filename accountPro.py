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
    with open(filename,"rb") as raw_input_file:
        try:
            return pickle.load(raw_input_file)
        except:
            return None

def pickle_dump(context,filename):
    with open(filename,"wb") as output_file:
        pickle.dump(context,output_file)

"""
userdata = {"username":"niehuawen","password":"2017!@#",1:{"Smoney":10000,"lend":0},2:{"Cmoney":0,"Check":0}}
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
    d_money = int(raw_input("how much you want to deposit ?").strip())
    #用户初始金额
    init_money = userdata[1]["Smoney"]
    #取钱后余额
    userdata[1]["Smoney"] = init_money - d_money
    #是否确定取钱操作
    flag = raw_input("Do you want to continue this deposit ops ? (y stand for continue)")
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
    w_money = int(raw_input("how much you want to withDraw ?").strip())
    # 用户初始金额
    init_money = userdata[1]["Smoney"]
    # 存钱后余额
    userdata[1]["Smoney"] = init_money + w_money
    # 是否确定存钱操作
    flag = raw_input("Do you want to continue this withdraw ops ? (y stand for continue)")
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
    l_money = int(raw_input("how much you want to lendBorrow ?").strip())
    # 用户初始金额
    init_money = userdata[1]["Smoney"]
    init_lend = userdata[1]["lend"]
    if l_money <= init_money:
        # 借钱后余额
        userdata[1]["Smoney"] = init_money - l_money
        userdata[1]["lend"] = init_lend + l_money
        # 是否确定借钱操作
        flag = raw_input("Do you want to continue this lendout ops ? (y stand for continue)")
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
    Enter Char [S D W L Q] Choice:"""
    while True:
        try:
            choice = raw_input(prompt).strip().lower()
        except:
            choice = "q"
        if choice not in "sdwlbq":
            choice == "q"
        elif choice == "s":
            #fname = raw_input("datafile:").strip()
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

#支票账号充值
def SaToCa(filename):
    #用户数据字典
    userdata = pickle_load(filename)
    #充值支票账号的金额
    c_money = int(raw_input("how much you want to check accout ?").strip())
    #存储账号初始金额
    init_money = userdata[1]["Smoney"]
    #支付账号初始金额
    Cinit_money = userdata[2]["Cmoney"]
    #取钱后余额
    if c_money <= init_money:
        userdata[1]["Smoney"] = init_money - c_money
        userdata[2]["Cmoney"] = Cinit_money + c_money
        # 是否确定支票账号充值操作
        flag = raw_input("Do you want to continue this SatoCa ops ? (y stand for continue)")
        if flag == "yes" or flag == "y":
            print("SaToCa money %s success!" % (c_money))
        # 取消支票操作时确定退回被减去的金额，防止多次取消操作导致大于原有存储账号的初始金额
        elif init_money == userdata[1]["Smoney"] + c_money and Cinit_money == userdata[2]["Cmoney"] - c_money:
            userdata[1]["Smoney"] = userdata[1]["Smoney"] + c_money
            userdata[2]["Cmoney"] = userdata[2]["Cmoney"] - c_money
    else:
        print("you must be smaller %s" % (init_money))
    #将数据写会至原文件
    pickle_dump(userdata,filename)

#支票账号至存储账号
def CaToSa(filename):
    #用户数据字典
    userdata = pickle_load(filename)
    #逆充值支票账号的金额
    r_money = int(raw_input("how much you want to check accout ?").strip())
    #存储账号初始金额
    init_money = userdata[1]["Smoney"]
    #支票账号初始金额
    Cinit_money = userdata[2]["Cmoney"]
    #取钱后余额
    if r_money <= Cinit_money:
        userdata[1]["Smoney"] = init_money + r_money
        userdata[2]["Cmoney"] = Cinit_money - r_money
        # 是否确定支票账号逆充值操作
        flag = raw_input("Do you want to continue this CatoSa ops ? (y stand for continue)")
        if flag == "yes" or flag == "y":
            print("SaToCa money %s success!" % (r_money))
        # 取消逆充值操作时确定退回被减去的金额，防止多次取消操作导致大于原有支票账号初始金额
        elif init_money == userdata[1]["Smoney"] - r_money and Cinit_money == userdata[2]["Cmoney"] + r_money:
            userdata[1]["Smoney"] = userdata[1]["Smoney"] - r_money
            userdata[2]["Cmoney"] = userdata[2]["Cmoney"] + r_money
    else:
        print("you must be smaller %s" % (Cinit_money))
    #将数据写会至原文件
    pickle_dump(userdata,filename)

#支票兑现至支票账号
def CheckToCa(filename):
    # 用户数据字典
    userdata = pickle_load(filename)
    # 支票兑现至支票账号的金额
    r_money = int(raw_input("how much you want to check accout ?").strip())
    # 支票账号初始金额
    init_money = userdata[2]["Cmoney"]
    # 支票金额
    Cinit_money = userdata[2]["Check"]
    #兑现金额小于支票金额且支票金额大于0
    if r_money <= Cinit_money and Cinit_money > 0:
        userdata[2]["Check"] = Cinit_money - r_money
        userdata[2]["Cmoney"] = init_money + r_money
        # 是否确定支票兑现操作
        flag = raw_input("Do you want to continue this ChecktoCa ops ? (y stand for continue)")
        if flag == "yes" or flag == "y":
            print("ChecktoCa money %s success!" % (r_money))
        # 取消支票兑现操作时确定退回被减去的金额，防止多次取消操作导致大于原有支票的初始金额
        elif init_money == userdata[2]["Cmoney"] - r_money and Cinit_money == userdata[2]["Check"] + r_money:
            userdata[2]["Check"] = userdata[2]["Check"] + r_money
            userdata[2]["Cmoney"] = userdata[2]["Cmoney"] - r_money
    else:
        print("ChecktoCa money must be smaller %s!" % (Cinit_money))
    # 将数据写会至原文件
    pickle_dump(userdata, filename)


#支票账号出支票
def CaToCheck(filename):
    # 用户数据字典
    userdata = pickle_load(filename)
    # 支票账户开支票的金额
    r_money = int(raw_input("how much you want to check accout ?").strip())
    # 支票账号初始金额
    init_money = userdata[2]["Cmoney"]
    # 原始支票金额
    Cinit_money = userdata[2]["Check"]
    # 开支票金额小于支票账户金额且支票账号金额大于0
    if r_money <= init_money and init_money > 0:
        userdata[2]["Check"] = Cinit_money + r_money
        userdata[2]["Cmoney"] = init_money - r_money
        # 确定是否开支票
        flag = raw_input("Do you want to continue this CaToCheck ops ? (y stand for continue)")
        if flag == "yes" or flag == "y":
            print("CaToCheck money %s success!" % (r_money))
        # 取消开支票操作时确定退回被减去的金额，防止多次取消操作导致大于原有支票账号的初始金额
        elif init_money == userdata[2]["Cmoney"] + r_money and Cinit_money == userdata[2]["Check"] - r_money:
            userdata[2]["Check"] = userdata[2]["Check"] - r_money
            userdata[2]["Cmoney"] = userdata[2]["Cmoney"] + r_money
    else:
        print("ChecktoCa money must be smaller %s!" % (Cinit_money))
    # 将数据写会至原文件
    pickle_dump(userdata, filename)


def CaOpsMenu():
    prompt = """
    (S)how cecking account 查看支票账号
    (R)echarge checking    充值支票账号
    (C)hecking to Storage  支票账号至存储账号
    (I)n checking          支票兑现至支票账号
    (O)ut checking         支票账号开支票
    (Q)uit     退出
    Enter Char [S R C Q I O Q] Choice:"""
    while True:
        try:
            choice = raw_input(prompt).strip().lower()
        except:
            choice = "q"
        if choice not in "srcqio":
            choice = "q"
        elif choice == "s":
            fname = "data.txt"
            if os.path.isfile(fname):
                show_account(fname,2)
        elif choice == "r":
            fname = "data.txt"
            if os.path.isfile(fname):
                SaToCa(fname)
        elif choice == "c":
            fname = "data.txt"
            if os.path.isfile(fname):
                CaToSa(fname)
        elif choice == "i":
            fname = "data.txt"
            if os.path.isfile(fname):
                CheckToCa(fname)
        elif choice == "o":
            fname = "data.txt"
            if os.path.isfile(fname):
                CaToCheck(fname)
        elif choice == "q":
            break

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
            choice = int(raw_input(prompt).strip())
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