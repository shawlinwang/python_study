'''
@author = xiaolin.wang
@description:

'''
import os
'''
os模块的某些函数是跟操作系统相关的
os.name
    获取系统名称
        windows: nt
        linux/mac/unix: posix
os.uname()
    系统详细信息
    但是windows系统不提供uname()方法
环境变量：
os.environ
    返回系统所有的环境变量
操作文件和目录
os.path
    abspath()   返回目录绝对路劲
    join()  拼接目录和文件
    split() 拆分目录和文件
    splitext() 拆分目录和文件后缀名
    dirname() 返回目标目录名称
新增/删除目录：
os.mkdir()
os.rmdir()
os.rename()
os.remove()
'''
base_dir = os.path.abspath('.')
base_file = os.path.abspath(__file__)
print(os.name)
# print(os.uname())
print(os.environ)
print(os.environ.get('PATH'))
print(os.path.abspath('..'))
print(os.path.abspath(__file__))
print(os.path.join(os.path.abspath('..'), 'functions', 'sorted.py'))
print(os.path.split(base_file))
print(os.path.splitext(base_file))
if __name__ == "__main__":
    pass
