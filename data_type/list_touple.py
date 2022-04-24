'''
@author = xiaolin.wang
@description:
列表和元祖
列表和元祖的差别在于，列表可以进行修改，元祖不可修改
'''

classmates = ['michael', 'bob', 'tracy']
classmates_touple = ('Michael', 'Bob', 'Tracy')


# 切片
print(classmates[0])
print(classmates[0:2])
print(classmates[2::-1])


# 添加/删除/拼接
classmates.append('shaw')
print(classmates)
classmates.insert(1, 'lily')
print(classmates)
# 列表拼接
c = ['xiaoming']
d = ['xiaoli', ]
classmates = classmates + c
print(classmates)
# extend 会返回None，最好不要直接取结果使用，例如：pritn(classmates.extend(d)) 会打印None
classmates.extend(d)
print(classmates)
print(classmates.pop())
print(classmates.pop(2))

# 排序
classmates.sort()
print(classmates)
print(sorted(classmates))


# 列表推导式
f = [i for i in range(10)]
print(f)