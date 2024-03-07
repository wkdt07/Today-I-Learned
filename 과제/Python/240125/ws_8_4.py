# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    
class Dog(Animal):
    sound2 = '멍멍'
    def bark(same):
        print(f'{same.sound2}!')     

class Cat(Animal):
    sound2 = '야옹'
    def meow(same):
        print(f'{same.sound2}!') 

class Pet(Dog,Cat):
    def __init__(self,sound):
        self.sound = sound

    def play(self):
        print('애완동물과 놀기')
    
    def make_sound(self):
        print(self.sound)

pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
