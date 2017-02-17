#!/usr/bin/env python
# -- coding:utf-8 --

"""
try:
    s = int(raw_input("input a number:"))
    print("hello world!")
    for number in range(s):
        print("number:%d" %(number))

except ValueError,e:
    print("Error reason:%s" %(e))
"""

def safe_open(filename):
    try:
        try:
            fd = open(filename)
        except BaseException,e:
            print("Error reason:%s" %(e))
            return None
        else:
            return fd
    finally:
        fd.close()

while True:
    input_file = raw_input("filename:").strip()
    fdesc = safe_open(input_file)
    print(fdesc)