'''
@author = xiaolin.wang
@description:
    Enum 枚举
'''

from enum import Enum
from enum import IntEnum, IntFlag

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan)

# value属性则是自动赋给成员的int常量，默认从1开始计数。
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

class IntMothEnum(IntEnum):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12

class MonthEnum(Enum):
    Jan = 1, '一月'
    Feb = 2, '二月'
    Mar = 3, '三月'
    Apr = 4, '四月'
    May = 5, '五月'
    Jun = 6, '六月'
    Jul = 7, '七月'
    Aug = 8, '八月'
    Sep = 9, '九月'
    Oct = 10, '十月'
    Nov = 11, '十一月'
    Dec = 12, '十二月'

for name, member in IntMothEnum.__members__.items():
    print(name, '=>', member, ',', member.value)
#
# for name, member in MonthEnum.__members__.items():
#     print(name, '=>', member, ',', member.value)
# print(MonthEnum.Jan.value[0])
# print(MonthEnum.Jan.value[1])
#
# print(MonthEnum.Jan.value)
# print(MonthEnum.Jan.name)