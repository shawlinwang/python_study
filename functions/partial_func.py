'''
@author = xiaolin.wang
@description:
partial 偏函数
'''
from functools import partial

# partial 有点类似于 linux系统的relias函数，制作一个别名函数


# 设定一个别名程序，调用int，给入参数base=2，后续可以直接采用int2
int2 = partial(int, base=2)

print(int2('1000000'))
