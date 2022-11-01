class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('sys'))

class Teacher(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Teacher object: (name: %s)' % self.name
        
print(Teacher('zhangsan'))