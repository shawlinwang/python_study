'''
@author = xiaolin.wang
@description:
    非常有用的用于操作迭代对象的函数
'''
import itertools
'''
itertools:
    count() 创建一个无限的迭代器
    cycle() 序列无限重复
    repeat() 一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
    takewhile() 函数根据条件判断来截取出一个有限的序列
    chain() 把一组迭代对象串联起来，形成一个更大的迭代器
    groupby() 迭代器中相邻的重复元素挑出来放在一起
'''
def count_func():
    natuals = itertools.count(1)
    for n in natuals:
        print(n)

def cycle_func():
    cs = itertools.cycle('ABC')
    for c in cs:
        print(c)

def repeat_func():
    cs = itertools.repeat('ABC', 3)
    for c in cs:
        print(c)

def takewhile_func():
    natuals = itertools.count(1)
    cs = itertools.takewhile(lambda x: x <= 10, natuals)
    print(list(cs))

def chain_func():
    cs = itertools.chain('ABC', 'XYZ')
    print(cs)
    for c in cs:
        print(c)

def groupby_func():
    cs = itertools.groupby('AaaBBbcCAAa', lambda c: c.upper())
    for key, group in cs:
        print(key, list(group))

def pi(N):
    ''' 计算pi的值 '''
    odds = itertools.count(1.0, 2)
    print(odds)
    ns = itertools.takewhile(lambda x: x <= 2 * N - 1, odds)
    flag, sum = 1, 0
    for number in ns:
        sum += 4 / number * flag
        flag = flag * -1
    return sum

if __name__ == "__main__":
    # count_func()
    # cycle_func()
    # repeat_func()
    # takewhile_func()
    # chain_func()
    # groupby_func()
    print(pi(100))
