'''
@author = xiaolin.wang
@description:

字典和集合
'''

# dict 是无须的，需要有序的字典，引用 from collections import OrderedDict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# 取值和设置
print(d['Michael'])
print(d.get('Michael', 0))
print(d.get('Michael1', 0))
d['Lily'] = 60
print(d)
# 抛出键值
print(d.pop('Michael'))

# 判断键是否存在
if 'Michael' in d:
    print(d['Michael'])

# 获取keys
print(list(d.keys()))

# 获取values
print(list(d.values()))

for key, value in d.items():
    print(key)
    print(value)


# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
s = set([1, 2, 3])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)