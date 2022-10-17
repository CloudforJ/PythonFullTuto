str1 = 'Hello, he is %s, and his salary is $%d' % ('zhangsan', 100000)
print(str1)

str2 = 'Hello, the improvement of {0} is {1:.1f}%'.format("zhangsan", 16.1256)
print(str2)

PI = 3.14
r = 2.5
s = PI * r ** 2
print(f'The area of the circle with r = {r} is {s:.2f}')