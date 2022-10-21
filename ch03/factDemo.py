def fact(n):
    if n == 1:
        return n
    return fact(n - 1) * n
    
print(fact(1))
print(fact(5))
print(fact(100))