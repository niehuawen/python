#!/usr/bin/env python
# -- coding:utf-8

def textrow(line):
    return line.strip()

fd = open("myfile.txt")
flist = map(textrow,fd)
fd.close()
"""
while True:
    try:
        flag = raw_input("new or old:").strip()
    except KeyboardInterrupt, e:
        print("Error reason:%s" % e)
    if flag not in ("new","old"):
        break
    elif flag == "new":
        filename = raw_input("new filename:").strip()
        fd = open(filename,"a+")
        for newline in flist:
            fd.write(newline+"\n")
        fd.close()
    else:
        fd = open("myfile.txt","w+")
        for newline in flist:
            fd.write(newline+"\n")
        fd.close()
"""

print(map(lambda line:line.strip(),open("myfile.txt")))