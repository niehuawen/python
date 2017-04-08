#!/usr/bin/env python
#--coding:utf-8--

import sqlite3
#连接至SQLite数据库
#数据库文件是test.db
#如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect("test.db")
#创建一个Cursor游标
cursor = conn.cursor()
#执行SQL语句。创建user表
#cursor.execute("create table user (id varchar(20) PRIMARY key,name varchar(20))")
#cursor.execute("insert into user (id,name) values ('1','niehuawen')")
#cursor.execute("insert into user (id,name) values ('2','niezhongwen')")
cursor.execute("insert into user (id,name) values ('3','guiyuanyuan')")
cursor.execute("insert into user (id,name) values ('4','zouhongying')")
#cursor.rowcount返回影响的行数
print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()

