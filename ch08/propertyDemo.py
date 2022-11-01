class Student(object):
    
    @property
    def score(self):
        return self._score
        
    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must be an integer")
        if score < 0 or score > 100:
            raise ValueError("score must between 0 - 100")
        self._score = score
        
s = Student()
s.score = 60
print(s.score)

s.score = 9999
print(s.score)