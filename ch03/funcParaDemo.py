def enroll(name, gender, age = 6, city = 'Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
    
print(enroll('Sarah', 'F'))
print(enroll('Bob', 'M', 7))
print(enroll('Adam', 'M', city='Tianjin'))

def calc(nums):
    sum = 0
    for n in nums:
        sum += n
    print(sum)
    
calc([1, 2, 3, 4])
calc((1, 2, 3, 4))

def cals(*nums):
    sum = 0
    for n in nums:
        sum += n
    print(sum)
    
cals(1, 2, 3, 4, 5)
num = [1, 3, 5, 76, 9]
cals(*num)

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('zhangsan', 13)
person('lisi', 18, city='beijing', salary=18000)
person('wangwy', 35, hobby='basketball')