'''
@author = xiaolin.wang
@description:
    hashlib: 提供了常见的摘要算法，如MD5，SHA1等等
        摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）
'''
import hashlib

def md5_func():
    md5 = hashlib.md5()
    md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
    print(md5.hexdigest().lower())
    print(md5.hexdigest().upper())
def md5_update_func():
    # 数据量很大，可以分块多次调用update()，最后计算的结果是一样
    md5 = hashlib.md5()
    md5.update('how to use md5 in '.encode('utf-8'))
    md5.update('python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())

'''
SH1： SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。

'''
def sh1_func():
    sha1 = hashlib.sha1()
    sha1.update('how to use sha1 in '.encode('utf-8'))
    sha1.update('python hashlib?'.encode('utf-8'))
    print(sha1.hexdigest())
if __name__ == "__main__":
    # md5_func()
    # md5_update_func()
    sh1_func()