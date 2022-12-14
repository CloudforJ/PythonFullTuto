def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
        
    if len(L) == 1:
        return (L[0], L[0])

    max = L[0]
    min = L[0]
    for i in L[1:]:
        if i > max:
            max = i
        if i < min:
            min = i
    return (min, max)



if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')