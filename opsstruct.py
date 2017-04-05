#!/usr/bin/env python
#--coding:utf-8--

#struct模块来解决str和其他二进制数据类型的转换
import struct
#">I" >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
#struct的pack函数把任意数据类型变成字符串
s = struct.pack(">I",10240099)
print(s)

#unpack把str变成相应的数据类型
t = struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')
print(t)