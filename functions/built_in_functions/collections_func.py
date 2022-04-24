'''
@author = xiaolin.wang
@description:
    collections
'''
'''
namedtuple:自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
from collections import namedtuple
'''
def namedtouple_func():
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p)
    print(type(p))
    print(p.x)
    print(p.y)
    print(list(p))

'''
deque:为了高效实现插入和删除操作的双向列表，适合用于队列和栈
    除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素
from collections import deque
'''
def deque_func():
    from collections import deque
    q = deque(['a', 'b', 'c'])
    q.append('d')
    q.appendleft('f')
    print(q)
    print(type(q))
    print(list(q))

'''
defaultdict: 默认值是调用函数返回的，而函数在创建defaultdict对象时传入
from collections import defaultdict
'''
def produce_defalt():
    # if key=='key2':
    #     return ""
    return None

def defaultdict_func():
    from collections import defaultdict
    def_dict = defaultdict(produce_defalt)
    def_dict['key1'] = None
    print(def_dict)
    print(type(def_dict))
    print(def_dict['key1'])
    print(def_dict['key2'])

'''
OrderedDict: 有序字典
from collections import OrderedDict
'''
def OrderedDict_func():
    from collections import OrderedDict
    d = dict([('b', 2),('a', 1), ('c', 3)])
    print(d)
    print(type(d))
    order_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print(order_dict)
    print(type(order_dict))

'''
ChainMap: 把一组dict串起来并组成一个逻辑上的dict, hainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找
from collections import ChainMap
'''
def ChainMap_func():
    from collections import ChainMap
    import os, argparse
    defaults = {
        'color': 'red',
        'user': 'guest'
    }

    # 构造命令行参数:
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-c', '--color')
    namespace = parser.parse_args()
    command_line_args = {k: v for k, v in vars(namespace).items() if v}

    # 组合成ChainMap:  依次放入命令参数集、环境变量、默认值
    combined = ChainMap(command_line_args, os.environ, defaults)

    # 打印参数:
    print('color=%s' % combined['color'])
    print('user=%s' % combined['user'])

'''
Counter：计数器，例如，统计字符出现的个数
from collections import Counter
'''
def Counter_func():
    from collections import Counter
    c = Counter()
    for ch in 'programming':
        c[ch] = c[ch] + 1
    print(c)
    print(type(c))
    c.update('hello')
    print(c)


if __name__ == "__main__":
    # namedtouple_func()
    # deque_func()
    # defaultdict_func()
    # OrderedDict_func()
    # ChainMap_func()
    Counter_func()