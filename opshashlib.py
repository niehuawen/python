#!/usr/bin/env python
#--coding:utf-8--

import hashlib
md5 = hashlib.md5()
md5.update("niehuawen,helloworld!")
print(md5.hexdigest())

#可以分多次调用update()
md5 = hashlib.md5()
md5.update("niehuawen,")
md5.update("helloworld!")
print(md5.hexdigest())

print("*"*50)

import hashlib
sha1 = hashlib.sha1()
sha1.update("1234567")
print(sha1.hexdigest())
#分多次调用update()
sha1 = hashlib.sha1()
sha1.update("niehuawen,")
sha1.update("helloworld!")
print(sha1.hexdigest())


user = {"niehuawen":"7c4a8d09ca3762af61e59520943dc26494f8941b",
        "niezhongwen":"20eabe5d64b0e216796e834f52d61fd0b70332fc"}

#用户验证登录函数
def login():
    while True:
        count = 0
        tag = 0
        username = raw_input("login username:")
        if username in user.keys():
            while count < 3:
                    password = raw_input("login password:")
                    sha1 = hashlib.sha1()
                    sha1.update(password)
                    sha1password = sha1.hexdigest()
                    if sha1password == user[username]:
                        print("congratuations to you.")
                        tag = 1
                        break
                    else:
                        count += 1
                        continue
            if tag == 1:
                break
        else:
            continue

if __name__ == "__main__":
    login()