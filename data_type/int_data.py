'''
@author = xiaolin.wang
@description:
整数类型
'''

# 二进制
binary = 0b1010
# 十进制相互转换函数 bin()
a = 10
print(bin(a))
print(int(binary))

# 十进制
decimal_system = 10

# 八进制
octal_number_system = 0o12
b = 10
print(oct(b))
print(int(octal_number_system))

# 十六进制
hexadecimal = 0xa
c = 10
print(int(hexadecimal))

# 大整数
big_int = 100000000000
big_int2 = 10_000_000_000
print(big_int)
print(big_int2)

# 可以使用not 对整数进行判断, not 0 返回 True
e = 0
e1 = -1
print(not e)
print(not e1)

# int 和 char 转换
f = 97
f1 = "0o12"
f2 = "0xa"
f3 = "0b1010"
f4 = "10"
f5 = "a"
print(str(f))
print(ord(f5))
print(int(f1, base=8))
print(int(f2, base=16))
print(int(f3, base=2))
print(int(f4, base=10))
