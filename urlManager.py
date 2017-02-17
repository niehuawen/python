#!/usr/bin/env python
# -- coding:utf-8 --

import re,sys

def Add():
    pass

def Modify():
    pass

def Delete():
    pass

def Find():
    pass

def Show():
    pass

def showMenu():
    prompt = """
    (A)dd url
    (M)odify url
    (D)elete url
    (F)ind url
    (S)how url
    (Q)uit
    Enter Choice:"""
    while True:
        try:
            choice = raw_input("your choice:").strip().lower()
        except ValueError,KeyboardInterrupt:
            choice = "q"
        if choice not in "amdfsq":
            choice = "q"
        elif choice == "a":
            Add()
        elif choice == "m":
            Modify()
        elif choice == "d":
            Delete()
        elif choice == "f":
            Find()
        elif choice == "s":
            Show()
        elif choice == "q":
            break
