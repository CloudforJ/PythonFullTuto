def f(x):
    return x * x

L = map(f, [x for x in range(10)])
print(L)
print(list(L))

from functools import reduce
def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))

def fn(x, y):
    return 10 * x + y

print(reduce(fn, [1, 3, 5, 7, 9]))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(list(map(char2num, '13579')))
print(reduce(fn, map(char2num, '13579')))


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return 10 * x + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

print(str2int('13578'))

def char2num1(s):
    return DIGITS[s]

# use lambda
def str2int1(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num1, s))

print(str2int1('12306'))


def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    def mul(x, y):
        return x * y
    return reduce(mul, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')