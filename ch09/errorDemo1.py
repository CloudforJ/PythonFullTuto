divideNum = int(input('please enter a num:'))
try:
    print('trying...')
    r = 10 / divideNum
    print('result:', r)
except ZeroDivisionError as e:
    print('error', e)
finally:
    print('finally')