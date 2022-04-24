'''
@author = xiaolin.wang
@description:

'''


'''
    struct模块来解决bytes和其他二进制数据类型的转换
        pack(): 把任意数据类型变成bytes
'''
import struct
print(struct.pack('>I', 10240099))
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
if __name__ == "__main__":
    pass
