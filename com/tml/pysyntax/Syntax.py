#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test module'
import sys

_author_ = 'tianmaolin'


def fun1(*a):
    print(a)


def fun2(**b):
    print(b)


# fun1(1, 2, 5)
# fun2(name='tianmlin', age=22)


def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello World!")
    elif len(args) == 2:
        print("Hello,%s!" % args[1])
    else:
        print("Too many arguments!")


if __name__ == '__main__':
    test()
