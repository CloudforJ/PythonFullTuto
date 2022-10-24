def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax
    
print(calc_sum(1, 3, 5, 7, 9))

def calc_sum1(**args):
    print('other:', args)
    
print(calc_sum1(city = 'Beijing', price = 12306))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum
    
f = lazy_sum(1, 3, 5, 7, 9)
f1 = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())
print(f == f1)

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
    
f2, f3, f4 = count()
print(f2())
print(f3())
print(f4())

def count1():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
    
f5, f6, f7 = count1()
print(f5())
print(f6())
print(f7())

