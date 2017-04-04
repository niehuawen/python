#!/usr/bin/env python
#--coding:utf-8--

#多线程同时修改变量，导致改乱balance解决方案
#修改变量前，必须先获得线程锁
#存在锁的多线程段代码是以单线程方式方式执行，即不能利用并发

import time,threading
#银行存款
balance = 0
lock = threading.Lock()

def change_it(n):
    #先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        #先要获取锁
        lock.acquire()
        try:
            #放心改吧
            change_it(n)
        finally:
            #改完了一定要释放锁
            lock.release()
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
time1 = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
time2 = time.time()
print(balance,time2-time1)
