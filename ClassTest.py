#!/usr/bin/env python
# --coding:utf-8 --

class Aclass(object):
    def __init__(self,age=18):
        self.age = age

    def showage(self):
        print("your age is %d:" %(self.age))

    def updateage(self,newage):
        self.age = newage

#如果子类没有定义__init__()构造函数，子类会默认调用父类的构造函数；如果子类定义了构造函数，则实例化时调用子类的构造函数
class Bclass(Aclass):
    def showinfo(self):
        print("Age:%d" %(self.age))

A = Aclass(10)
B = Bclass()
A.updateage(20)
A.showage()
B.showinfo()