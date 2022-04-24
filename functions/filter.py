'''
@author = xiaolin.wang
@description:
filter 用于过滤序列
'''


# filter()也接收一个函数和一个序列， 传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
# 返回一个 filter对象，是筛选数据后的 filter 对象，集成于 Iterator
def is_odd(n):
    return n % 2 == 1


print(filter(is_odd, [1, 2, 3, 4, 5, 6]))
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))
