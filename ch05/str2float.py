from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'10': 10}

def str2float(s):
    i = s.index('.')
    s1 = s[:i]
    s2 = s[i+1:]
    def char2num(x):
        return DIGITS[x]
    def str2int(s):
        return reduce(lambda x, y: x * 10 + y, map(char2num,s))
    result = str2int(s1) + str2int(s2) * pow(10, -i)
    return result

#测试
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
