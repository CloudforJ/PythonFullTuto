L = ['Micheal', 'jack', 'sarah', 'bob', 'jason']

r = []
n = 3
for i in range(n):
    r.append(L[i])

print(r)

def trim(str):
    if len(str)==0:
       return str
    elif str[0] == ' ':
       str = str[1:]
       return trim(str)
    elif str[-1]== ' ':
       str = str[:-1]
       return trim(str)
    else: 
       return str


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
