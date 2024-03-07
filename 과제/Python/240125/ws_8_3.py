class Animal:
    num_of_animal = 0

class Cat(Animal):
    def __init__(same,meow):
        same.sound = meow
    
    def meow(same):
        print(f'{same.sound}!')

cat1 = Cat("야옹")
cat1.meow()
