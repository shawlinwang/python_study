'''
@author = xiaolin.wang
@description:
sorted 排序
'''

# sorted()函数对list进行排序, 还可以接收一个key函数来实现自定义的排序

# 按绝对值排序
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))