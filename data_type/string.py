'''
@author = xiaolin.wang
@description:
字符串
'''

a = "a"
b = '''
test b
'''

# 转换
c = 'I\'m \"OK\"!'

# 字符串拼接
print(a + b + c)

# 格式化输出
print("this is format %s" % "test")
print("this is format {}".format("test"))

# 切片
print(c[:2])
print(c[0:7:3])

# 迭代
for i in c:
    print(i)

# 迭代器进行迭代
it = iter(c)
print(it.__next__())

# 字符串判断, 空字符串能被not进行空校验, 但是 " "不能被校验
e = ""
e1 = "1"
print(not e)
print(not e1)