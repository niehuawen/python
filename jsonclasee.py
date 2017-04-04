#!/usr/bin/env python
#--coding:utf-8--

import json

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
def student2dict(std):
    return {
        "name":std.name,
        "age":std.age,
        "score":std.score
    }
s = Student("Bob",29,88)
#如果不定义student2dict函数，json不知道如何将Student类实例序列化为json对象,得到json对象j
#j = json.dumps(s,default=student2dict)
#或者采取偷懒的做法如下
j = json.dumps(s,default=lambda obj:obj.__dict__)
print("type of %s is : %s" %(j,type(j)))

print("*"*50)
#将json对象反序列化为python实例对象
def dict2student(d):
    return Student(d["name"],d["age"],d["score"])
json_str = '{"age":20,"score":88,"name":"Bob"}'
print(json.loads(json_str,object_hook=dict2student))

