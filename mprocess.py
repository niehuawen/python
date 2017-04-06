#!/usr/bin/env python
#--coding:utf-8--

from multiprocessing import Process
import os

#子进程执行的代码
def run_proc(name):
    print("Run child process %s(%s)..." %(name,os.getpid()))

if __name__ == "__main__":
    print("Parent process %s." % os.getpid())
    #Process调用，target、args参数，target参数为函数名，args为target函数的元组形式参数
    p = Process(target=run_proc,args=("test",))
    print("Process will start.")
    p.start()
    #真正的执行在p.start()之后
    print(1)
    #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    print(2)
    print("Process end.")