# class Person:
#     # 속성(=변수)
#     blood_color = 'red'


#     #메서드 
#     def __ini__(self,name):
#         self.name = name
    
#     def singing(self):
#         return f'{self,name}가 노래합니다.'
    


# # 인스턴스 생성

# # singer1 = Person('hi')


# class Person:
#     name = 'unknown'
#     # 생성자 함수가 없음
#     def talk(self):
#         print(self.name)

# p1 = Person()
# p1.talk()
# # 현재 인스턴스 변수 name이 없어서 
# #클래스에서 찾아서 unknown이 나옴

# p2 = Person()
# p2.name = 'kim' # 이제 p2한테 인스턴스 변수가 할당됨
# p2.talk()

# print(Person.name) #unknown
# print(p1.name) #얘는 본인게 없어서 class의 변수인 unknown이 출력
# print(p2.name)

# p2.ssafy = 11
# print(p2.ssafy) #p2에 또다시 새로운 인스턴스 이름공간을 만들어서 할당한거임
# #독립적인 거임. name 안 맞춰도 됨




# #=============================================================

# ''' 실습 : 생성자 메서드 구조로 class Singer 선언 후
# 1. 인스턴스 속성 출력
# 2. 인스턴스 메서드 호출
# '''
# #SHB
# class Singer:
#     job = '직업: 가수'
#     date = '생년월일: 1993년 5월 16일'
#     country = '국적: 대한민국'

#     def __init__(self,name):
#         self.name = name

#     def 랩(self):
#         print('랩하기')

#     def 댄스(self):
#         print('댄스 추기')

#     def 소몰이(self):
#         print('소몰이 부르기')
    

# singer1 = Singer('IU') 

# #1. 인스턴스 속성 출력 -> 속성은 멤버 변수로 
        

# print(singer1.job)
# print(singer1.date)
# print(singer1.country)

# #2. 인스턴스 메서드 호출 -> 행동(동작)은 메서드로 

# singer1.랩()
# singer1.댄스()
# singer1.소몰이()

# #------------------#

# #강사님

# class Singer:
#     #여기에 선언되면 클래스 변수
#     def __init__(self): #생성자 메서드
#         self.occ = '가수' #멤버 변수
#         self.birth = '1993년 5월 16일'
#         self.nat = '대한민국'
    
#     def rap(self): #인스턴스 메서드 : self 매개변수를 통해 해당 객체에 접근
#         print('랩 하기')
    
#     def dance(self):
#         print('댄스 추기')
    
#     def sing(self):
#         print('소몰이 부르기')


# #클래스 인스턴스 생성
# singer = Singer()

# #인스턴스 속성 출력
# print('직업:',singer.occ)
# print('생년월일:',singer.birth)
# print('국적:',singer.nat)

# #인스턴스 메서드 호출
# singer.rap()
# singer.dance()
# singer.sing()


'''
### 실습2 
my_count라는 메서드 직접 만들기
클래스명은 my_str

조건 1. 생성자 매서드 구조
조건 2. 클래스 변수와 멤버 변수 생성
조건 3. 기능은 count() 메서드와 같은 기능
'''


# class my_str:
#     def __init__(self,name):
#         self.name = name #str로 만들기 위해 여기서 인스턴스 변수를 할당
#         self.count = 0
        

#     def my_count(self,alp):
#         self.count = 0
#         for char in self.name:
           
#             if char == alp:
#                 self.count += 1
#                 # count += 1
#             # else: 
#             #     continue
#         return self.count

# banana = my_str('banana')

# print(banana.my_count('n'))
# print(banana.my_count('a'))


#====================================================#

# ### 실습 3

# 실습 1에서 했던걸 복붙해서 클래스 메서드만으로 구성되도록 바꾸기


# class Singer:
#     job = '직업: 가수'
#     date = '생년월일: 1993년 5월 16일'
#     country = '국적: 대한민국'

#     @classmethod
#     def func(cls):
#         print(f'{cls.job}\n{cls.date}\n{cls.country}')
#         print('랩하기')
#         print('댄스 추기')
#         print('소몰이 부르기')
# Singer.func()

# class Singer:
    
#     #여기에 선언되면 클래스 변수

#     def __init__(self): #생성자 메서드 : 인스턴스 변수들의 초기값을 설정

#         self.occ = '가수' #멤버 변수 == 인스턴스 변수
#         self.birth = '1993년 5월 16일'#멤버변수
#         self.nat = '대한민국'#멤버변수
    
#     #인스턴스 메서드 구조: 객체(인스턴스)의 속성에 접근할 수 있으며, self 매개변수를 통해 해당 객체에 접근한다. 
#     def rap(self): 
#         print('랩 하기')
    
#     def dance(self):
#         print('댄스 추기')
    
#     def sing(self):
#         print('소몰이 부르기')



#================================
# ### 실습 4 스태틱 메서드로 실습 1 바꾸기
# : 클래스나 인스턴스와는 무관하게 독립적으로 동작하는 메서드
# (클래스 내부에서 선언되지만 클래스 변수에 접근하지 않는다)


class Singer:
    
    @staticmethod
    def rap(): 
        print('랩 하기')

    @staticmethod
    def dance():
        print('댄스 추기')

    @staticmethod
    def sing():
        print('소몰이 부르기')


Singer.rap()
Singer.dance()
Singer.sing()