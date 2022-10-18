names = ['tom', 'jack', 'jerry']
for name in names:
    print(name)
    
sum = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += i
print(sum)

print(list(range(5)))

# calculate sum from 0 to 100(include)
sum = 0
for i in range(101):
    sum += i
print(sum)

sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("hell0, ", name, "!")
    

# use break
n = 0
while n < 100:
    if n > 10:
        break
    print(n)
    n += 1
    
# use continue
m = 0
while m < 100:
    m += 1
    if m % 2 == 0:
        continue
    print(m)