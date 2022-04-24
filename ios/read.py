'''
@author = xiaolin.wang
@description:

'''
import os

base_path = os.path.dirname(os.path.abspath(__file__))
text_file = os.path.join(base_path, 'text.txt')

with open(text_file, 'r') as f:
    for line in f.readlines():
        it = iter(line)

        work = it.__next__()
        print(line)

if __name__ == "__main__":
    pass
