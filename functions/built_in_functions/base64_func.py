'''
@author = xiaolin.wang
@description:
    base64:
        Base64是一种用64个字符来表示任意二进制数据的方法。
        Base64是一种最常见的二进制编码方法
        Base64编码会把3字节的二进制数据编码为4字节的文本数据
        Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等
'''
import base64
print(base64.b64encode(b'binary\x00string'))
# 标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))
if __name__ == "__main__":
    pass
