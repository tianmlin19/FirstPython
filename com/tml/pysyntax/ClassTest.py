#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test module'
from com.tml.pysyntax.ClassDemo import Student

student = Student('haozi', 88)
student.printName()

print(isinstance(student, Student))

print(type(student))

print(student)

student