a = input('pls enter an int num: ')
try:
    print('try...')
    r = 10 / int(a)
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('No error')
finally:
    print('Finally...')
print('END')