#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test module'


class Student(object):
    __slots__ = ('__name', '__score')

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def printName(self):
        print('%s:%s' % (self.__name, self.__score))

    def __str__(self):
        return 'Student (name:%s,score:%s)' % (self.__name,self.__score)
