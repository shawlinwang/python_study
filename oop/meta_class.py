'''
@author = xiaolin.wang
@description:
    元类
    metaclass，直译为元类

    先定义metaclass，就可以创建类，最后创建实例。
    所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
'''

# type(类) 返回 <class 'type'>
# type(实例), 返回<class '__main__.Hello'> 引用类
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

class Hello2(Hello):
    pass

# metaclass是类的模板，所以必须从`type`类型派生：
# 按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        '''
            __new__()方法接收到的参数依次是：
                当前准备创建的类的对象；
                类的名字；
                类继承的父类集合；
                类的方法集合。
        '''
        attrs['add'] = lambda self, value: self.append(value)  # 新建一个add 方法, 把value插入 self实例对象
        return type.__new__(cls, name, bases, attrs)

# 传入关键字参数metaclass时,Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
class MyList(list, metaclass=ListMetaclass):
    pass

# 通过 type() 创建类
if __name__ == "__main__":
    # h = Hello()
    # h2 = Hello2()
    # print(isinstance(Hello, type))
    # print(isinstance(Hello, object))
    # print(isinstance(Hello, Hello))
    # print(type(Hello))
    # print(type(Hello2))
    # print(type(h))
    # print(type(h2))
    # print(issubclass(Hello2, Hello))
    #
    # # 通过 type() 创建类
    # def fn(self, name='world'):
    #     print('Hello, %s.' % name)
    # Hello3 = type('Hello3', (object,), dict(hello=fn))
    # print(type(Hello3))
    # h3 = Hello3().hello()
    L = MyList()
    L.add(1)