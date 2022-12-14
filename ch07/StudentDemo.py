class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def print_score(self):
        print('%s, %s' % (self.name, self.score))
        
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >=70 and self.score < 90:
            return 'B'
        else:
            return 'C'
        
bart = Student('bart', 78)
lisa = Student('Lisa', 99)
bart.print_score()
lisa.print_score()
print(bart.name, bart.get_grade())
print(lisa.name, lisa.get_grade())