#!/usr/bin/env python
# -- coding:utf-8 --
# description: file() 或者 open()函数
# 参数：文件名字符串和打开方式字符串"a+"|"rw"|"r+"|"a+"
# 返回：文件对象描述符

#方式一
ft = file("test.txt","r+")
for line in ft:
    print(line.strip())
ft.close()

print("*"*40)

#方式二
with open("test.txt","r+") as ff:
    for line in ff:
        print(line.strip())
