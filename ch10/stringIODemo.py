from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

f1 = StringIO('Hello!\nHi\nGoodbye!')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())