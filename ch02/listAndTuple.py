# list
classmates = ['tom', 'jack', 'jerry']
for classmate in classmates:
    print(classmate)
    
classmates.append('zhangsan')
classmates.insert(1, 'wangwu')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)

# tuple, cannot be changed after define
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

t = (1, 2)
print(t)

k = (1, )
print(k)

