#!/usr/bin/env python
#--coding:utf-8--

import os

#os.getpid()获取当前进程pid
print("Process (%s) start..." % os.getpid())
#os.fork()返回两次，父进程返回子进程pid，子进程返回0。
pid = os.fork()
#根据pid是否为0，区分是父进程还是子进程返回
#pid为0,表示为子进程返回
if pid == 0:
    print("I am child process (%s) and my parent is %s." %(os.getpid(),os.getppid()))
#pid不为0，表示父进程返回
else:
    print("I (%s) just created a child process (%s)." %(os.getpid(),pid))
