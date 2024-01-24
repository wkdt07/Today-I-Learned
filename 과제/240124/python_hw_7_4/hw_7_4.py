# 아래 클래스를 수정하시오.
class Person:
    number_of_people = 0
    num = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.number_of_people += 1
        Person.num += 1

    def introduce(self):
        print(f'제 이름은 {self.name}이고, 저는 {self.age}살입니다.')
    # @classmethod
    # def number(cls):
    #     return cls.num

person1 = Person("Alice", 25)
person1.introduce()
print(Person.number_of_people)
# print(Person.number()) 만약 위에서 함수로 return하고 싶었다면 여기처럼 ( ) 넣어줘야함

