'''
@author = xiaolin.wang
@description:
    @contextmanager
    如果一个对象没有实现上下文，我们就不能把它用于with语句
'''
from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

# 受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

# 用closing()来把该对象变为上下文对象
from contextlib import closing
from urllib.request import urlopen
def python_org_func():
    with closing(urlopen('https://www.python.org')) as page:
        for line in page:
            print(line)

if __name__ == "__main__":
    with create_query('Bob') as q:
        q.query()

    python_org_func()