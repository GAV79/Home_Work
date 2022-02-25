# задача 1
from sys import argv

path, var1, var2, var3 = argv
a = map(int, argv[1:])


def func(args):
    hour, gold_hour, premia = args
    zp = hour * gold_hour + premia
    return zp


res = func(a)
print(f'ЗП сотрудника = {res}')

# задача 2
a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
b = [a[i] for i in range(1, len(a)) if a[i] > a[i-1]]
print(b)

#  задача 3
a = [el for el in range(20, 240) if el % 21 == 0]
print(a)

# задача 4
a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
b = [a[i] for i in range(len(a)) if a.count(a[i]) == 1]
print(b)

# задача 5
from functools import reduce

b = [el for el in range(10, 1001) if el % 2 == 0]


def f1(vr1, vr2):
    return vr1 * vr2


d = reduce(f1, b)
print(d)

# задача 6
from itertools import count, cycle
b = []
for el in count(3, 2):
    if el > 24:
        break
    else:
        b.append(el)
print(b)
k = 0
for i in cycle(b):
    print(i)
    k += 1
    if k > 15:
        break

# задача 7
from math import factorial


def fact(n):
    for el in (i for i in range(1, n + 1)):
        yield factorial(el)


for al in fact(5):
    print(al)
