'''
@author = xiaolin.wang
@description:
条件判断
'''

# 常用判断 if ，搭配 not is == 等判断符

# python内||采用 or  &&采用 and
a = "a"
b = "b"
if a == "a" or b == "c":
    print(True)
if a == "a" and b == "c":
    print(True)

'''
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
'''

# if elif 的模式，可以用作平替java等语言的 switch