import functools
from email.mime import base
from functools import reduce

from asn1crypto import keys


def f(x):
    return x * x


def g(x, y):
    return x + y


def formatName(kk):
    return kk.title()


def is_odd(n):
    return n % 2 == 1


i = map(f, [1, 2, 6])
print(list(i))

reduce1 = reduce(g, [1, 2, 6])
print(reduce1)

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))


# 判断一个数字是不是回数
def is_palindrome(m):
    mm = str(m)
    return mm == mm[::-1]


print(list(filter(is_palindrome, range(1, 200))))

print(list(sorted([23, 12, 45, 8, -36], key=abs)))

# 排序
print(list(sorted(['Bob', 'tom', 'Jack', 'amy'], key=str.lower, reverse=False)))

print(list(map(lambda x: x * x, [1, 2, 3, 6])))

partial = functools.partial(int, base=2)
print(partial('11111111'))
