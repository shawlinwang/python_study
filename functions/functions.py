'''
@author = xiaolin.wang
@description:
函数
'''
#
# # 定义函数和调用
# def add(x, y):
#     return x+y
#
# print(add(1, 2))
#
# # 参数，必填参数，选填参数
# def sub(x, y , z=0):
#     return x-y-z
#
# print(sub(6,5,2))

# *arg, **kwargs
def arg_func(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)

arg_func(1, 2, 3, 4, 5, c=5, d=6, e=7)
#
#
# # lambda 函数
# x = lambda x :10 if True else 0
# print(x)
# print(lambda x :10 if True else 0)
#
#
# # 递归函数
# def fact(n):
#     print(n)
#     if n==1:
#         return 1
#     return n * fact(n - 1)
# fact(10)