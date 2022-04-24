'''
@author = xiaolin.wang
@description:
    哈希算法: Hmac算法：Keyed-Hashing for Message Authentication
'''
import hmac

def hmac_func_():
    message = b'Hello, world!'
    key = b'secret'
    h = hmac.new(key, message, digestmod='MD5')
    print(h.hexdigest())
if __name__ == "__main__":
    hmac_func_()
