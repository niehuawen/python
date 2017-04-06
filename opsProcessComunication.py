#!/usr/bin/env python
#--coding:utf-8--

#进程间通信，使用Queue队列，一个进程往Queue中写数据，两个一个进程往Queue中读数据

from multiprocessing import Process,Queue
import os,time,random

#写数据进程执行的代码
def write(q):
    for value in ["A","B","C"]:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())

#读数据进程执行的代码
def read(q):
    while True:
        value = q.get(True)
        print("Get %s from queue." % value)

if __name__ ==  "__main__":
    #父进程创建Queue，并传递给各个子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    #启动子进程pw，写入
    pw.start()
    #启动子进程pr,读取
    pr.start()
    #等待pw结束
    pw.join()
    #pr进程里是死循环，无法等待期结束，智能强行终止
    pr.terminate()
