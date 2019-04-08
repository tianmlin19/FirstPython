#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'文件io'
import os

with open('C:\\Users\\admin\Desktop\\tmp\\tianmlin.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())#去掉结尾的换行


print(os.environ)