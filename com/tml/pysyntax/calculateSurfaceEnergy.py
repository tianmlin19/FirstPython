#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Copyright:    WZP
Filename:     calculateSurfaceEnergy.py
Description:

@author:      wuzhipeng
@email:       763008300@qq.com
@website:     https://wuzhipeng.cn/
@create on:   10/12/2021 16:46
@software:    PyCharm
"""

# 导入sympy库
from sympy import *
from sympy.abc import a,b

def calculate(theta1,theta2):
    Symbol('a')
    Symbol('b')
    
    eq1 = (87.2*a)/(a+21.8)+(204*b)/(b+51)
    eq2 = (148*a)/(a+37)+(105.6*b)/(b+26.4)
    
    S = solve([eq1-(1+cos(theta1))*72.8,eq2-(1+cos(theta2))*63.4],[a,b])

    print(S)
    return S


# theta1,theta2 = 110.65,100.45
# S = calculate(theta1,theta2)
#
# for a, b in S:
#     print(f'a={a}')
#     print(f'b={b}')
#
#     print((87.2*a)/(a+21.8)+(204*b)/(b+51)-(1+cos(theta1))*72.8, (148*a)/(a+37)+(105.6*b)/(b+26.4)-(1+cos(theta2))*63.4)

x,y=symbols('x y')

# f1=2*sqrt(21.8*x)+2*sqrt(51*y) - 72.8*(1+cos(104.9*pi/180))
# f2=2*sqrt(37*x)+2*sqrt(26.4*y) - 63.4*(1+cos(78.3*pi/180))

f1=4*21.8*x/(x+21.8)+4*51*y/(y+51)-72.8*(1+cos(104.9*pi/180))
f2=4*37*x/(x+37)+4*26.4*y/(y+26.4)-63.4*(1+cos(78.3*pi/180))

solve([f1,f2],[x,y])