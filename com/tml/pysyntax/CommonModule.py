#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'python内建模块'
from datetime import datetime

now = datetime.now()
print(now)

dt = datetime(2018, 12, 13, 18, 51, 26)
print(dt)
# 使用timestamp()获取的是小数，小数部分表示的是毫秒数
print(now.timestamp())
strptime = datetime.strptime('2018-12-13 15:26:25', '%Y-%m-%d %H:%M:%S')
print(strptime)

print(now.strftime('%a, %b %d %H:%M'))
