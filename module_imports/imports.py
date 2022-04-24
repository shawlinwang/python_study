'''
@author = xiaolin.wang
@description:
import 导入
'''

# 写入作者名称
__author__ = 'xiaolin.wang'


'''
包目录下 需要带 __init__.py 文件
'''


'''
包导入的两种方式
    import time
    from functools import reduce
'''


'''
包导入别名
    from time import time as time_now
'''

# 内置模块和已安装包 路劲打印
import sys
import os
print(sys.path)

# 可以手动插入 sys.path 来添加包
# 此方法只能在python运行过程中进行修改，运行结束后，会自动消失
dir_path = os.path.dirname(os.path.abspath(__file__))   # __file__ 指当前文件，python魔术方法
print(dir_path)
sys.path.append(dir_path)   # 把当前文件目录插入python 的path
for path in sys.path:
    print(path)


import requests