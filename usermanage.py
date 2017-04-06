#!/usr/bin/env python
#--coding:utf-8--

import hashlib
db = {}

def register(username,password):
    sha1 = hashlib.sha1()
    str = username + password + "salt2017"
    sha1.update(str)
    encrptstr = sha1.hexdigest()
    db[username] = encrptstr
    print("%s register success!" % (username))

def login(username,password):
    if username in db.keys():
        sha1 = hashlib.sha1()
        str = username + password + "salt2017"
        sha1.update(str)
        encrptstr = sha1.hexdigest()
        if db[username] == encrptstr:
            print("login success...")
        else:
            print("password error...")
    else:
        print("user not existed!")

def show():
    for user in db.keys():
        print(user)

def menu():
    prompt = """
    1.register
    2.login
    3.show
    """
    print(prompt)

if __name__ == "__main__":
    while True:
        menu()
        try:
            choice = raw_input("your choice:").strip().lower()
        except KeyboardInterrupt,ValueError:
            break
        if choice == "1":
            name = raw_input("username:").strip()
            if name not in db.keys():
                password = raw_input("password:").strip()
                register(name,password)
            else:
                print("%s user existed!")
        elif choice == "2":
            name = raw_input("username:").strip()
            password = raw_input("password:").strip()
            login(name,password)
        elif choice == "3":
            show()
        elif choice == "quit":
            break
        else:
            continue