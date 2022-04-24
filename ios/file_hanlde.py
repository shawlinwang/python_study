'''
@author = xiaolin.wang
@description:

    文件处理，文件IO
'''
import os

base_path = os.path.dirname(os.path.abspath(__file__))
text_file = os.path.join(base_path, 'text.txt')

'''
    open() 方法用于打开文件
        第一个参数为 文件
        第二个参数为 读写方式，一般常用  r读   w写  rb二进制读  wb二进制写
        encodint 设置指定读取编码方式
        errors 设置是否忽略错误
        内存的字节流，网络流，自定义流等等 都可以采用open(),然后使用read()进行读取
'''


def file_read():
    with open(text_file, 'r', encoding='gbk', errors='ignore') as f:
        print(f.read())


def file_write():
    with open(text_file, 'w', encoding='gbk', errors='ignore') as f:
        desc = "新写入内容"
        desc.encode()
        desc.encode('gbk')
        print(desc)
        f.writelines(desc)


'''
    with 详解：
        with所求值的对象必须有一个enter()方法，一个exit()方法
        
    比如说，数据库连接就可以用with来完成， 调用自动连接，执行完成自动关闭
'''


class Sample:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''
            __exit__()方法负责执行“清理”工作，如释放资源等。
                如果执行过程中没有出现异常，或者语句体中执行了语句break/continue/return，则以None作为参数调用__exit__(None, None, None)；
                如果执行过程中出现异常，则使用sys.exc_info得到的异常信息为参数调用__exit__(exc_type, exc_value, exc_traceback)

                出现异常时，如果__exit__(type, value, traceback)返回False，则会重新抛出异常，让with之外的语句逻辑来处理异常，这也是通用做法；
                如果返回True，则忽略异常，不再对异常进行处理
        '''
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        return True         # 可以切换True和False返回来查看执行结果，是否会打印异常堆栈信息
        # return False

    def do_something(self):
        bar = 1 / 0
        return bar + 10


def do_thins():
    with Sample() as sample:
        sample.do_something()


if __name__ == "__main__":
    # file_read()
    # file_write()
    do_thins()
