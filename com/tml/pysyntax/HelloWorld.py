from builtins import print, range, TypeError

print(ord('张'))

print(chr(24352))

print('田茂林'.encode('utf-8'))
print(b'\xe7\x94\xb0\xe8\x8c\x82\xe6\x9e\x97'.decode("utf-8"))
print(len('田茂林'))
print('%d-%02d' % (35555, 1))
print('%.2f' % 3.1415926)

classmate = ['tianmaolin', '吕布', '孙悟空']
print(classmate[2])
classmate.pop(0)
classmate.insert(1, '张飞')
classmate.append('刘备')
print(classmate)

listaa = ('青龙偃月刀', '方天画戟', '百鸟朝凤枪', '青釭剑', ['aaa', 'bbb'])
# listaa[0]='屠龙刀'--tuple元组是不允许修改的
listaa[4][0] = 'cccc'
print(listaa)

age = 1
if age >= 18:
    print("your age is:", age)
    print("adult")
elif age > 6:
    print("your age is ", age)
    print("teenager")
else:
    print("your age is ", age)
    print("kids")

# int()函数
print(int(2.86))

# for --in 遍历
for a in listaa:
    print(a)

# range()函数生成[0,a-1]范围内的数字
print(list(range(10)))
sum = 0
for x in range(101):
    sum += x
print(sum)

n = 1
sum_tmp = 0
while n <= 100:
    sum_tmp += n
    n += 1
print("sum_tmp:", sum_tmp)

# break语法
m = 0
while m < 100:
    if m == 6:
        break
    print("m=", m)
    m += 1

# continue语法
m = 0
while m < 10:
    m += 1
    if m % 2 == 0:
        continue
    print(m)

# dictionary的用法,相当于java中的map
print("--------------------------")
map = {"tianmlin": 12, "zjie": 13, "kk": 16}
print("tianmlin" in map)
print(map.get("tianmlin2", 0))
print("删除之前", map)
map.pop("tianmlin")
print("删除之后", map)

print(abs(-12.35612))


def printHello(aa):
    if not isinstance(aa, str):
        raise TypeError("bad parameter type")
    print("hello", str)


