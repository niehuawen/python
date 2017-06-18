#!/usr/bin/env python
# -- coding:utf-8 --
# input and output
name = raw_input("your name:")
age = int(raw_input("your age:"))
student = {}
# python 2.x
print "name:%s" % name
# python 3.x
print("name:%s" % name)
print("name:%s" % (name))
print("name:{0}".format(name))

# python 2.x
print "age:%s" % age
# python 3.x
print("age:%s" % age)
print("age:%s" % (age))
print("age:{0}".format(age))

# python 2.x
print "name:%s\nage\t:%s" % (name,age)
# python 3.x
print("name:%s\nage\t:%s" % (name,age))
print("name:{0}\nage\t:{1}".format(name,age))
print("name:{name}\nage\t:{age}\nsex\t:{sex}\naddress\t:{address}".format(name="gui yuanyuan",age=29,sex="G",address="GuanZhou HaiZhu"))