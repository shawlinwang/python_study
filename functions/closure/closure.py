'''
@author = xiaolin.wang
@description:
closure 闭包
'''

def count():
    def f():
        return 1
    return f
print(count)
print(count())
print(count()())
# a = count()
# print(a)
# print(a())
#
#
# # 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)   # 注意这里，插入的是一个 f 的引用，并不是调用
#     return fs
#
# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())
#
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())
#
# # 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。
# def inc():
#     x = 0
#     def fn():
#         nonlocal x
#         x = x + 1   # 如果不声明 nonlocal x， 这一行就相当于在 申明一个变量x，但是没有初始值，所以 x+1会报错
#         return x
#     return fn
#
# f = inc()
# print(f()) # 1
# print(f()) # 2