'''
@author = xiaolin.wang
@description:
字符串和编码
'''
a = "a"
b = "中文"
c = "中文"
e = b'ABC'
# 字节流
print(b.encode())
# python 默认编码 UTF-8
print(b.encode().decode('UTF-8'))
# 字符编码 ASCII （-128~127）
print(a.encode('UTF-8').decode('ASCII'))
print(e.decode("ASCII"))
# python的字符串str ，在内存以 unicode进行存储
print(c)
