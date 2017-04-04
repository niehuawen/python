#!/usr/bin/env python
#--coding:utf-8--

import json

d = dict(name="Bob",age=29,score=88)
#python对象d通过dumps()序列化返回字符串s1 json对象
s1 = json.dumps(d)
print("type of %s : %s" %(s1,type(s1)))
f = open("t1.txt","wb")
#dump()序列化至文件
json.dump(d,f)
f.close()

#loads()反序列化，输入为字符串json对象context,返回python对象s1
f = open("t1.txt","rb")
context = f.read()
s1 = json.loads(context)
print("type of %s : %s" %(s1,type(s1)))
f.close()

#load()反序列化，输入为文件描述符，返回python对象s2
f = open("t1.txt","rb")
s2 = json.load(f)
print("type of %s : %s" %(s2,type(s2)))
f.close()

