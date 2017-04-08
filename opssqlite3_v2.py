#!/usr/bin/env python
#--coding:utf-8--

import sqlite3

try:
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("select * from user where id = ? and name = ?",("1","niehuawen"))
    results = cursor.fetchall()
    for result in results:
        print(result)
except Exception,e:
    print(e)
finally:
    cursor.close()
    conn.close()