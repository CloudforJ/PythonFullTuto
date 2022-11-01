class Student(object):
    def get_score(self):
        return self._score
        
    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must be an integer")
        if score < 0 or score > 100:
            raise ValueError("score must between 0 - 100")
        self._score = score
        
s = Student()
s.set_score(60)
print(s.get_score())

s.set_score(12306)
print(s.get_score())