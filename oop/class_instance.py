'''
@author = xiaolin.wang
@description:

'''


class Student(object):
    a = 1

    def __new__(cls, *args, **kwargs):
        print("new")
        return super().__new__(cls, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print(2)


    def __init__(self):
        print("__init__")
        self.a=2
        # self.name = name
        # self.score = score
        # self.__sex = sex
        # self._id_no = 1233414   # _xxx 单下划线为约定行为私有变量，可引用修改，但是尽量不要这样做]

    @classmethod
    def class_method(cls):
        print(1)

    def instance_method(self):
        print(2)

    # def print_score(self):
    #     print(self.score)
    #
    # def get_sex(self):
    #     return self.__sex

if __name__ == "__main__":
    # print(Student)
    # stu = Student("xiaolin", 30, "男")
    # print(stu)
    # stu.print_score()
    # # stu.__sex      # 直接访问 __xx 变量，解释器报错 AttributeError
    # stu._Student__sex  # 采用特殊引用方式，访问 __xx变量
    # stu.__sex = "女"   # 对__xx 的私有变量进行修改，实际是给 stu新增了一个 __sex变量，原有实例instance的__sex实际是 instance._Student__sex
    # print(stu.get_sex())
    # print(dir(stu))
    # print(stu.__getattribute__('__sex'))    # 此处打印出来的则是修改后的变量值： 女
    # print(stu._id_no)
    # Student
    print(Student)
    print(Student())
    def fn():
        pass
    print(fn)
    print(fn())
    # a = Student()
    # a.instance_method()

    # print(dir(Student))