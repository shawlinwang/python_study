'''
@author = xiaolin.wang
@description:
decorator 装饰器
'''
import time


# 在代码运行期间动态增加功能的方式，称之为“装饰器”， decorator就是一个返回函数的高阶函数


# def log(func):
#     def wrapper(*args, **kw):
#         print('call {}:'.format(func.__name__))
#         return func(*args, **kw)
#     return wrapper
#
# # 这里只是 采用装饰器，将now传入到log内，最终返回func() 的调用
# @log
# def now():
#     print('2015-3-25')
# now()
#
# print(dir(now))
#
# 二层包裹，装饰器接受参数

def log_new(*ar, **kw):  # 第一层装饰器接受的参数是装饰器参数
    # print(ar)
    # print(kw)
    # print('2')
    print(1)

    def decorator(func):
        def wrapper(*args, **kwargs):  # 第二层装饰器接受的参数是被调用函数体给入的参数
            print(args)
            print(kwargs)
            # print('1')
            # print(time.time())
            # result = func(*args, **kwargs)
            # print(time.time())
            # return result
            now = time.time()
            a = func(*args, **kwargs)
            end = time.time()
            print(end - now)
            return a
        # print('4')
        return wrapper

    # print('3')
    return decorator
# def test():
#     print('-------------')
#     print("我被执行了")
# print(log_new(1, 2, 3, c=4, d=5)(test)())
@log_new(1, 2, 3, c=4, d=5)
def now_new(*args, **kwargs):
    return "6666"
#
#
# print(log_new)
# print(log_new(1, 2, 3, c=4, d=5))

# f = now_new
# print(f)
# f(6, 7, 8, 9, d=10, f=11)


if __name__ == "__main__":
    pass


