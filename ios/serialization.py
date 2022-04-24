'''
@author = xiaolin.wang
@description:
    序列化
'''

'''
pick实现序列化
    将内存数据写入到 物理硬盘
'''
import pickle
d = dict(name='shaw', age=20, score=88)
with open('text.txt', 'bw') as f:
    print(pickle.dump(d, f))    # 直接用dump写入文件
print(pickle.dumps(d))
with open('text.txt', 'br+') as f:
    print(pickle.load(f))
with open('text.txt', 'br+') as f:
    data = f.readline()
    print(pickle.loads(data))

'''
JSON:
数据映射：
    {}	            dict
    []	            list
    "string"	    str
    1234.56	        int或float
    true/false	    True/False
    null	        None
'''
import json
d = dict(name='shaw', age=20, score=88)
print(json.dumps(d))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

# json处理中文
json_str = '{"age": 20, "score": 88, "name": "小林"}'
print(json.loads(json_str))
# python内部以unicode编码存储数据，json.dumps输出中文添加 ensure_ascii=False
dict = {"age": 20, "score": 88, "name": "小林"}
print(json.dumps(dict))
print(json.dumps(dict, ensure_ascii=False))

if __name__ == "__main__":
    pass
