#!/usr/bin/env python
# --coding:utf-8--
import os

def find(keystr,path="."):
    apath = os.path.abspath(".")
    #使用os.walk递归子目录
    for dir_path,subpath,files in os.walk(apath):
        for file in files:
            if keystr in file:
                print(os.path.join(dir_path,file))

if __name__ == "__main__":
    find("ex")
