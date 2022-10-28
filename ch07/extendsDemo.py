class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Dog is eaTING...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

    def eat(self):
        print('Cat is eating...')
dog = Dog()
cat = Cat()
dog.run()
cat.run()