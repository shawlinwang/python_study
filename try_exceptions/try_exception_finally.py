'''
@author = xiaolin.wang
@description:
    try...except...finally...
'''
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')


# 跨层级捕获
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
        raise Exception('Error:', e)
    finally:
        print('finally...')
# def main():
#     bar('0')
if __name__ == "__main__":
    main()
