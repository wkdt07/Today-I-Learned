# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    


class Dog(Animal):
    def __init__(same):
        # print(same.num_of_animal)
        # same.num_of_animal += 1 #0->1 #Dog의 속성에 새로운 num_of animal이 생긴거임. 클래스 변수엔 영향을 주지 않음
        Animal.num_of_animal += 1#init 매서드에서 클래스 변수에 접근하려면 클래스명.클래스변수명 으로 접근해야한다. (init 매서드 특징)
        # print(same.num_of_animal)
         


class Cat(Animal):
    def __init__(same):
        # print(same.num_of_animal)
        Animal.num_of_animal += 1
        # print(same.num_of_animal)
        


class Pet(Dog,Cat):
    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {cls.num_of_animal}마리 입니다.'
    


dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())

