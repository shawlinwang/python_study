'''
@author = xiaolin.wang
@description:
    多进程
'''

'''
    Unix/Linux操作系统提供了一个fork()系统调用
        fork()调用一次，返回两次，返回一个父进程，一个子进程
        子进程永远返回0，而父进程返回子进程的ID
        父进程可以fork出很多子进程， 子进程只需要调用getppid()就可以拿到父进程的ID
'''
import os

# # linux/unix 系统
# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''
    from multiprocessing import Process
        p.start() 启动进程
        join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
'''
from multiprocessing import Process

def run_proc(name):
    print(name)
    print("运行子进程： {} {}".format(name, os.getpid()))


def main_mul():
    print('运行父进程 %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')


'''
    Pool 进程池
'''
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def main_pool():
    print('Parent process %s.' % os.getpid())
    # p = Pool(4)
    # for i in range(5):
    #     p.apply_async(long_time_task, args=(i,))
    # print('Waiting for all subprocesses done...')
    # p.close()
    # p.join()          # 加上join() 后，系统会等待进行执行完成后，再执行后续
    # print('All subprocesses done.')
    with Pool(4) as p:
        p.map(long_time_task, [1,2,3,4])
    p.join()
    print('All subprocesses done.')


'''
subprocess 子进程
    call() 调用子进程执行， 控制输入输出
'''
import subprocess

def subprocess_call():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)

def subprocee_popen():
    '''
    communicate
        与进程交互：将数据发送到stdin并关闭它, 返回一个元组（stdout，stderr）
    :return:
    '''
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('gbk').encode().decode('utf-8'))
    print('Exit code:', p.returncode)

'''
进程间通信
    Queue:
        在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
'''
from multiprocessing import Process, Queue
import os, time, random
# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)
def queue_start():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
if __name__ == "__main__":
    # main_mul()
    # main_pool()
    # subprocess_call()
    # subprocee_popen()
    queue_start()