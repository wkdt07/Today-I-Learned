# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    
class Dog(Animal):
    sound2 = '멍멍'
    def bark(same):
        print('멍멍!')   

class Cat(Animal):
    sound2 = '야옹'
    def meow(same):
        print('야옹!') 

class Pet(Dog,Cat):
    def __init__(self,sound):
        self.sound = sound

    def play(self):
        print('애완동물과 놀기')
    
    def make_sound(self):
        print(self.sound)

    def __str__(self):
        return f'애완동물은 {self.sound2} 소리를 냅니다.'

pet1 = Pet("그르르")
print(pet1)