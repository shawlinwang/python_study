'''
@author = xiaolin.wang
@description:

    StringIo
'''
from io import StringIO
from io import BytesIO

# StringIO 读写
# StringIO顾名思义就是在内存中读写str
def string_io_i():
    f = StringIO()
    f.write('hello')
    f.write(' ')
    f.write('world!')
    print(f.getvalue())

def string_io_o():
    f = StringIO('Hello!\nHi!\nGoodbye!')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())

def byte_io_i():
    f = BytesIO()
    f.write('中文'.encode('utf-8'))
    print(f.getvalue())

def byte_io_o():
    f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    print(f.read())

if __name__ == "__main__":
    string_io_o()
    string_io_i()
    byte_io_i()
    byte_io_o()

