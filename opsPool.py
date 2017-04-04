#!/usr/bin/env python
#--coding:utf-8--

#当需要大量创建子进程时使用Pool方式

from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print("Run task %s %s" %(name ,os.getpid()))
    start = time.time()
    time.sleep(random.random()*5)
    end = time.time()
    print("Task %s runs %0.2f seconds" %(name,end-start))

if __name__ == "__main__":
    print("Parent process %s." % os.getpid())
    #Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。
    #Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。
    #可以修改为其他数字如6
    p = Pool(6)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print("Waiting for all subprocesses done...")
    p.close()
    #join()之后真正调用执行
    p.join()
    print("All subprocesses done.")