'''
@author = xiaolin.wang
@description:
__slots__ slots方法
'''


class Student:
    __slots__ = ('name', 'age')

class GraduateStudent(Student):
    pass

if __name__ == "__main__":
    a = Student()
    a.name = "a"
    a.age = 10

    print(a.__slots__)

    b = GraduateStudent()
    b.score = 30