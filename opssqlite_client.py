#!/usr/bin/env python
#--coding:utf-8--

import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("select id,name from user where id=? or name=?",("1","zouhongying"))
#cursor.fetchall()返回列表
values = cursor.fetchall()
for value in values:
    print(value)
print(values)
cursor.close()
conn.close()
