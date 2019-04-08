#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'枚举类'
from enum import Enum, unique

MON = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


@unique
class WeekDay(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# for name, number in MON.__members__.items():
#    print(name, number,number.value)

print(WeekDay.Fri.value)
