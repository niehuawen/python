#!/usr/bin/env python
#--coding:utf-8--

#Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等

#Base64编码会把3字节的二进制数据编码为4字节的文本数据
#如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
import base64
b64 = base64.b64encode("binary\x00string")
print(b64)

#"\x00"表示一个字节,显示为空格
b64 = base64.b64encode("\x00")
print(b64)

b46 = base64.b64decode("YmluYXJ5AHN0cmluZw==")
print(b46)
rb46 = base64.b64decode("AA==")
print(rb46)

#"url safe"的base64编码
#标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_

u64 = base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print(u64)
ru64 = base64.urlsafe_b64decode("abcd--__")
print(ru64)
