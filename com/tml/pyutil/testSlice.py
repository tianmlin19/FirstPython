L = list(range(100))
# 获取list中前10个元素
print(L[:10])
# 获取list中后10个元素
print(L[-10:])
print(L[::5])


def trim(str):
    if len(str) == 0:
        return ''
    elif str[:1] == ' ':
        return trim(str[1:])
    elif str[-1:] == ' ':
        return trim(str[:-1])
    else:
        return str


def findMinAndMax(LL):
    if not LL:
        return None, None
    else:
        min = LL[0]
        max = LL[0]
        for item in LL:
            if (item > max):
                max = item
            if (item < min):
                min = item
        return min, max


# 列表生成式
kk = [x * x for x in range(1, 10) if x % 2 == 1]
kk = [m + n for n in 'ABC' for m in 'CDE']
L = ['Hello11', 'World22', 'IBM', 'Apple', 188]
L = [s.lower() for s in L if isinstance(s, str)]
print(L)


# 高阶函数，一个函数可以接收另外一个函数作为参数
def caculateTwoNumber(a, b, f):
    return f(a, b)


def add(a, b):
    return a + b


def multipy(a, b):
    return a * b


print(caculateTwoNumber(3, -5, multipy))
