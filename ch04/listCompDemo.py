L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

X = [x * x for x in range(10)]
print(X)

Y = [m + n for m in 'XYZ' for n in 'ABC']
print(Y)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)
    
cor = ['Hello', 'worLd', 'IBM', 'Apple']
cors = [s.lower() for s in cor]
print(cors)

evenNum = [x for x in range(100) if x % 2 == 0]
print(evenNum)

ifelselist = [x if x % 2 == 0 else -x for x in range(10)]
print(ifelselist)