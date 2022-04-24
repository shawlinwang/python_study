'''
@author = xiaolin.wang
@description:

    multiple inheritance  多重继承
'''


class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass
    # def common_func(self):
    #     print("Mammal")

class Bird(Animal):
    pass
    # def common_func(self):
    #     print("Bird")


# MixIn 是python多继承实现内 将 主继承以外的 额外功能写入 通用MixIn 类的设计模式

class RunnableMixIn(object):
    def run(self):
        print('Running...')

    def common_func(self):
        print("RunnableMixIn")


class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

    def common_func(self):
        print("FlyableMixIn")


class CarnivorousMixIn(object):
    def eat(self):
        print("吃肉")

    def common_func(self):
        print("CarnivorousMixIn")


class HerbivoresMixIn(object):
    def eat(self):
        print("吃草")

    def common_func(self):
        print("HerbivoresMixIn")


# 各种动物:
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass


class Parrot(Bird, FlyableMixIn, HerbivoresMixIn):
    pass


if __name__ == "__main__":
    dog = Dog()
    dog.run()
    dog.eat()

    parrot = Parrot()
    parrot.eat()
    parrot.fly()

    # 如果出现多继承，父类拥有相同的方法，那么实例调用方法会依次采用引入顺序内的第一个父类方法
    dog.common_func()
    parrot.common_func()