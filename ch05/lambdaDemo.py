print(list(map(lambda x : x * x, [x for x in range(10)])))
f = lambda x : x * x
print(f)
print(f(5))


L = list(filter(lambda x : x % 2 == 1, range(1, 20)))
print(L)