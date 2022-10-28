class Animal(object):
    def run(self):
        print("Animal is running...")
        
    def eat(self):
        print("Animal is eating...")
        
class Dog(Animal):
    def run(self):
        print("Dog is running...")
    def eat(self):
        print("Dog is eating...")
        
class Cat(Animal):
    def run(self):
        print("Cat is running...")
    def eat(self):
        print("Cat is eating...")
        
def run_twice(animal):
    animal.run()
    animal.run()
    
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())