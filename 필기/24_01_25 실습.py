# #딕셔너리에서 키를 조회할 때 키가 없다는 상황을 2개로 만들어본다.

# my_dict = {}

# #1) try - except

# try:
#     result = my_dict['a'] #일단 때려박고 시작
#     print(result)
# except:
#     print('key가 존재하지 않습니다.')

# #2) if-else

# if 'a' not in my_dict: #한 번 확인하고 시작
#     result = my_dict['a']
#     print(result)    
# else:
#     print('key가 존재하지 않습니다.')


# '''
# 결과는 같지만 코드의 스타일은 전혀 다르다.

# 우린 문제 해결을 거의 해본적이 없어서 1위주로 했음

# 2는 문제 해결을 위한 것

# '''

#=========================================#
##offlint

# #<다중상속>

# class Car:
#     def __init__(self,model):
#         self.model = model


# class Hyundai(Car):
#     color = 'white'

#     def speed(self):
#         return "30km/h"

# class Kia(Car):
#     color = "black"
    
#     def engine(self):
#         return '1.6 turbo'

# class CarDrive(Hyundai,Kia):
#     def speed(self):
#         return '50km/h'
    
#     def power(self):
#         return '1.999cc'
    
# car = CarDrive('Sonata')
# print(car.speed()) #메서드 호출  #50km/h

# print(car.color) #클래스 변수 접근 #white


# '''
# 메서드 호출: 가장 마지막에 호출된 애가 나온다.

# 클래스 변수 접근: 먼저 상속된 애(Hyundai)
# '''

#================================================#

# < 다이아몬드 상속 >
# class A:
#     def __init__(self):
#         print('A Constructor')


# class B(A):
#     def __init__(self):
#         super().__init__()
#         print('B Constructor')


# class C(A):
#     def __init__(self):
#         super().__init__()
#         print('C Constructor')


# class D(B, C):
#     def __init__(self):
#         super().__init__()
#         print('D Constructor')


# obj = D()
# A Constructor
# C Constructor
# B Constructor
# D Constructor

# class A:
#     def __init__(self):
#         print('A Constructor')


# class B(A):
#     def __init__(self):
#         super().__init__() 
#         print('B Constructor')


# class C(A):
#     def __init__(self):
#         super().__init__()
#         print('C Constructor')


# class D(C, B):
#     def __init__(self):
#         super().__init__()
    
#         print('D Constructor')

# obj = D()


# def calculate_sum(a,b):
#     return a+b

# numbers =[1,2,3,4,5]
# result = 0

# #만약 result = [] 로 한다면? TypeError
# for i in range(len(numbers)):
    
#     result = calculate_sum(result,numbers[i]) # i = 0 일 때 result가 할당이 안 되어있다.
# #NameError , result를 초기화해야한다. 
# print(result)


# def my_index(arr,index):
#     try:
#         result =arr[index]
#     except IndexError:
#         result = None

#     return result


# my_list = [1,2,3,4,5]
# index_1 = int(input())
# element = my_index(my_list,index_1)
# print(element)

class Animal:
    num_of_animal = 0
    def __init__(same):
        Animal.num_of_animal += 1
    
class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Pet(Dog,Cat):
    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {cls.num_of_animal}마리 입니다.'
    


dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())
