'''
@author = xiaolin.wang
@description:
生成器， 迭代器
'''

# # 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
# L = [x * x for x in range(10)]
# print(L)
# g = (x * x for x in range(10))
# print(g)
# print(g.__next__())
#
# # generator的另一种方法,函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator函数，调用一个generator函数将返回一个generator
# def fib1(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# f1 = fib1(6)
# print(f1)
#
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield n
        # a, b = b, a + b
        n = n + 1
    return 'done'

def add(a):
    return a+1
f = fib(6)
f.__next__()
a = 1
add(a)
f.__next__()
# print(f)
# flag = True
# while flag:
#     try:
#         print(f.__next__())
#     except StopIteration:
#         print("结束了")
#         flag=False



# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())





from collections.abc import Iterable, Iterator
# 生成器都是Iterator对象
# list、dict、str虽然是Iterable，却不是Iterator
# 使用 iter() 将 Iterable 转换为 Iterator
# Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误
# a = 10
# b = "1213123"
# # print(isinstance(a, Iterable))
# # print(isinstance(b, Iterable))
#
# str = "sasdasfsdg test zasfsdfds test"
# it = iter(b)
# print(it)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# for i in b:
#     print(i)