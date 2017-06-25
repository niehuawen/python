#!/usr/bin/env python
# -- coding:utf-8 --
#

import os

ls = os.linesep

def write2file():
    fname = raw_input("please input a filename:")
    while True:
        if os.path.exists(fname):
            print("ERROR: %s already exists" % fname)
        else:
            break

    all = []
    print("\nEnter lines ('.' by itself to quit).\n")

    while True:
        entry = raw_input('>')
        if entry == '.':
            break
        else:
            all.append(entry)

    fobj = open(fname,"w")
    fobj.writelines(["%s%s" % (x,ls) for x in all])
    fobj.close()


def readfile():
    while True:
        frname = raw_input("please input a filename:")
        try:
            fd = open(frname,"r")
        except IOError as e:
            print(e)
        else:
            for line in fd:
                print(line.strip())
            fd.close()
            break

def editfile():
    while True:
        fename = raw_input("please input a filename you want to edit:")
        try:
            os.system("vim fename")
        except:
            break

CMDs = {"w":write2file,"r":readfile,"e":editfile}

prompt = """
    (w)rite to file
    (r)ead from file
    (e)dit file
    (q)uit
    Your Choice:"""

def main():
    while True:
        print(prompt),
        try:
            choice = raw_input().strip()[0].lower()
        except IndexError,KeyboardInterrupt:
            choice = 'q'
        if choice in "wre":
            CMDs[choice]()
        else:
            break

if __name__ == "__main__":
    main()

