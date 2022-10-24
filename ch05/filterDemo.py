def is_odd(n):
    return n % 2 == 1
    
print(list(filter(is_odd, [x for x in range(10)])))

def not_empty(s):
    return s and s.strip()
    
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))