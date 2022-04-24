'''
@author = xiaolin.wang
@description:
实例属性、类属性
'''


class Student:
    score = 0

    def __init__(self, name, score, sex):
        self.name = name
        self.score = score

    def print_score(self):
        print(self.score)

class Student2:
    score = 0

    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    stu = Student("xiaolin", 30, "男")
    stu2 = Student("shaw", 20, "女")
    print(stu.score)
    print(stu2.score)
    print(Student.score)
    Student.score = 1
    print(Student.score)
    stu.score=60
    stu2.score=70
    print(stu.score)
    print(stu2.score)
    print(Student.score)


    stu3 = Student2('a')
    print(stu3.score)
    stu3.score = 60
    print(stu3.score)
    print(Student2.score)