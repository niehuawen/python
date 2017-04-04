#!/usr/bin/env python
# --coding:utf-8--
import codecs
import os

with open("textfile.txt","r") as fd1:
    print(fd1.read())

#windows平台文本文件的汉字默认为"gbk"编码，所以读取时使用decode("gbk")解码
with open("binaryfile.txt","r") as fd2:
    print(fd2.read().decode("gbk"))

#同上，调用codecs模块的另一种写法
with codecs.open("binaryfile.txt","r","gbk") as fd3:
    print(fd3.read())

print("*"*50)
with codecs.open("binarytest","wb") as fd4:
    fd4.write("爱你们，Jeffrey.nie2")

with codecs.open("binarytest","rb") as fd5:
    print(fd5.read())