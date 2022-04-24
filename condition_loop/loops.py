'''
@author = xiaolin.wang
@description:
循环
'''

# a = [1, 2, 3, 4, 5]
# for i in a:
#     print(i)
#
# print(list(range(5)))
# # while 判断
# flag = True
# n = 1
# while flag:
#     print(n)
#     n += 1
#     if n > 10:
#         flag = False
#
# import sys  # 引入 sys 模块
#
# # 迭代器
# list = [1, 2, 3, 4]
# it = iter(list)  # 创建迭代器对象
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


# 迭代器搭配生成器，费布拉奇数组
import sys
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
