'''
@author = xiaolin.wang
@description:
map  reduce
'''
from functools import reduce


# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# map 函数返回一个 map对象，继承于Iterator，可以进行遍历，所有采用list打印数据
def squre(n):
    return n * n

def add(x, y):
    print(x)
    print(y)
    return x + y

print(map(squre, [1, 2, 3, 4, 5]))
print(list(map(squre, [1, 2, 3, 4, 5])))

# reduce把一个函数作用在一个序列上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce 直接返回函数最终计算结果
print(reduce(add, [1, 3, 5, 7, 9]))
