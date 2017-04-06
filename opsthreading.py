#!/usr/bin/env python
#--coding:utf-8--

import time,threading

#子线程执行的代码
def loop():
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("thread %s >>> %s" % (threading.current_thread().name,n))
        time.sleep(1)
    print("thread %s ended." % threading.current_thread().name)

#主线程执行的代码
print("thread %s is running..." % threading.current_thread().name)
#主线程调用子线程
t = threading.Thread(target=loop,name="LoopThread")
t.start()
t.join()
print("thread %s ended." % threading.current_thread().name)