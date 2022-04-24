'''
@author = xiaolin.wang
@description:
布尔值和None
'''

# 布尔包含 False 和 True， 可以使用 is 和 not 进行对象判断
bool_1 = False
bool_2 = True
print(not "")
print(not 0)
print(not {})
print(not [])
print(not 0.00)


class C:
    pass


print(not C())
