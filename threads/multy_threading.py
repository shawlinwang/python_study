'''
@author = xiaolin.wang
@description:
多线程:
    Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装
'''
import random
import time, threading
'''
    多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
    而多线程中，所有变量都由所有线程共享，
    所以，任何一个变量都可以被任何一个线程修改，
    因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
'''
# 新线程执行的代码:
this_var = "这是一个变量"
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    global this_var
    if threading.current_thread().name == 'Thread-2':
        this_var = '这是被线程2改变的变量'
    while n < 5:
        print(this_var)
        n = n + 1
        print('thread %s >>> %s\n' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

def start_thread():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop)
    t2 = threading.Thread(target=loop)
    t.start()
    t2.start()
    t.join()
    t2.join()
    print('thread %s ended.' % threading.current_thread().name)

'''
线程锁：
    Lock
'''
balance = 0
def change_it(n):
    global balance    #声明全局变量
    balance = balance + n
    balance = balance - n

def change_range(n, lock):
    for i in range(20000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
            # pass
def thread_run():
    lock = threading.Lock()
    t1 = threading.Thread(target=change_range, args=(5, lock))
    t2 = threading.Thread(target=change_range, args=(8, lock))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)

if __name__ == "__main__":
    # start_thread()
    thread_run()
