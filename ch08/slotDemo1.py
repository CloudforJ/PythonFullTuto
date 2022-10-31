class Student(object):
    __slots__ = ('name', 'age')
    
s = Student()
s.name = 'zhangsan'
print(s.name)
s.age = 16
print(s.age)
# will be error because __slots__ not include feature score
#s.score = 99
#print(s.score)

# parent class __slots__ will not affect child class
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 99
print(g.score)