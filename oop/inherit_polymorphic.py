'''
@author = xiaolin.wang
@description:
inherit_polymorphic   继承和多态
'''

# python内所有的 类都继承于 object

class Animals:
    def run(self):
        print('Animal is running...')

'''
Dog 和 Cat 在继承了 Animals之后，各自都实现run() 方法， 在类和实例中会覆盖父类的 run() 方法， 这种方式叫做多态 polymorphic
'''
class Dog(Animals):
    def run(self):
        print('Dog is running...')

class Cat(Animals):
    def run(self):
        print('Cat is running...')


# 鸭子类型： 对于Python这样的动态语言来说，只需要保证传入的对象有一个run()， 并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
class Timer(object):
    def run(self):
        print('Start...')

def run_twice(animal):
    animal.run()
    animal.run()

if __name__ == "__main__":
    print(Animals.__base__)    # 会打印 object

    dog = Dog()
    cat = Cat()

    dog.run()
    cat.run()

    run_twice(dog)
    run_twice(cat)

    timer = Timer()
    run_twice(timer)
