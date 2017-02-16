#!/usr/bin/env python
# -- coding:utf-8 --

import cPickle as pickle
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
userdata = {"username":"niehuawen","password":"2017!@#",1:{"Smoney":10000}}
pickle_dump(userdata,"data.txt")
p = pickle_load("data.txt")
for key in p:
    print(key,p[key])
"""

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

def deposit_money(filename):
    userdata = pickle_load(filename)
    d_money = int(raw_input("how much you want to deposit ?").strip())
    init_money = userdata[1]["Smoney"]
    userdata[1]["Smoney"] = init_money - d_money
    flag = raw_input("Do you want to cacel this deposit ops ?(y stand for cacel)")
    if flag == "yes" or flag == "y" and init_money == userdata[1]["Smoney"] + d_money:
        userdata[1]["Smoney"] = userdata[1]["Smoney"] + d_money
    pickle_dump(userdata,filename)

def SaOpsMenu():
    prompt = """
    (S)how Storage account 查看
    (D)eposit money 取钱
    (W)ithdraw 存钱
    (L)end out 借出
    (B)orrow   借入
    (Q)uit     退出
    Enter Char [S D W L B] Choice:"""
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
            pass
        elif choice == "l":
            pass
        elif choice == "b":
            pass
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