# a = ' Practice makes perfect '

# #1. 문자열 a에서 'e'의 개수 세기 ***

# print(a.count('e'))

# #2. 문자열 a에서 i의 위치 찾기(2가지 방법)*****

# print(a.index('i'))

# print(a.find('i'))

# #3. 문자열 a의 문자 사이에 .(점) 삽입
# print(a.replace(' ','.'))

# #4. 문자열 a를 공백 기준으로 분리하기
# print(a.split(' '))

# #5. 문자열 a에서 'makes'를 'made'로 바꾸기
# print(a.replace('makes','made'))

# #6. 문자열 a를 대문자에서 소문자로 바꾸기, 소문자에서 대문자로 바꾸기
# b=a.swapcase()
# print(b)

# c=b.swapcase()
# print(c)
# #7. 문자열 a의 양쪽 공백 삭제하기
# print(a.strip())

# #8. 입력된 시간(14:43:20)에서 시간 부분만 보여주기

# t='14:43:20'
# t_1 = t.split(':')[0]
# print(t_1)


# #8-1 주민등록번호 (890927-1212121)에서 생일만 보여주기. 성별 보여주기

# birth = '890927-4212121'

# print(birth.split('-')[0][2:])

# if print(birth.split('-')[1][0]) == (1 or 3):  #왜 이거 뒤에 괄호 없으면 female이 안 나오지?
#     print('Male')
# else: 
#     print('Female')


##==================================


# a=['b','a','n','a','n']

# # 1. 리스트 a의 마지막에 'a' 추가하기

# a.append('a')
# print(a)

# # 2. 

# # #2-1. 리스트 a를 오름차순으로 정렬 -> 원본 변경
# # a.sort()
# # print(a)

# #2-2. 리스트 a를 오름차순으로 정렬 -> 원본 변경하지 않는다
# # print(sorted(a))
# b = a[:]
# b.sort()
# print(b)
# print(a)

# # 3. 리스트 a를 내림차순으로 정렬
# b = a
# b.sort(reverse=True)
# print(b)

# # 4. 리스트 a를 역순으로 뒤집기
# a.reverse()
# print(a)

# # 5. 리스트 a에서 문자 'a'를 삭제하기
# for i in range(a.count('a')):
#     a.remove('a')
# print(a)


# #========================================

# # 6. 리스트 a의 마지막 요소를 꺼내서 삭제하고 반환값 출력

# b = a.pop()
# print(b)
# # 7. 리스트 a에서 문자 'n'의 갯수 출력
# print(a.count('a'))


##=============================================

# #24.01.23

# not_set = {} # : 빈 딕셔너리


# void_set = set() # : 빈 세트

# my_set = { 'a', 'b', 'c', 1, 2, 3}

# print(my_set) # {'c', 1, 2, 3, 'a', 'b'} 
# 순서가 없어서 실제 출력은 나열 x
# 배치시 정해진 순서에 따른 key가 만들어지긴 함. 이건 이후 파트에서

# # .add(x) ,append와 비슷하지만 얘는 리스트와 다르게 순서가 없음. 마지막에 넣지 x

# my_set.add(4)

# print(my_set)

# my_set.add(4) # 한 번 더 반복하면?

# print(my_set) # 똑같다. 중복 x, 교재엔 'd' 넣은 걸로 나옴


# # .clear()

# my_set.clear()

# print(my_set) # set() -> 터미널에도 빈 세트는 이렇게 출력

# my_set.remove('a') # 'a' 지워짐``

# print(my_set)

# my_set.remove('a')

# print(my_set)  # KeyError: 'a' , 없는걸 지우려 하면 에러가 남 


# # pop() -> 인자를 안 넣으면 마지막 거가 제거되는게 리스트, 여기선 *'임의의'* 요소를 반환 
# # why? 순서가 없기 떄문


# element =  my_set.pop() #임의의 요소가 제거되고 반환됨
# print(element)
# ##왜 임의가 아닌거 같은지 다시 강의 봐라 졸았음.

# my_set_2 = {'a','b','c','d','e'} 
# element_2 =my_set_2.pop()
# print(element_2)

# #.update(iterable) == extend()

# my_set.update([1,4,5]) #중복된건 안 들어간다. 오류가 나진 x

# print(my_set)

# # #discard() : 오류 없는 remove()

# my_set.discard('z')

# print(my_set) # 오류 안 나고, 그냥 위에 있는 my_set과 같음

## 세트 메서드
# set1 = {0,1,2,3,4}
# set2 = {1,3,5,7,9}

# print(set1.difference(set2)) #{0, 2, 4}
# print(set1.intersection(set2)) #{1, 3}
# print(set1.issubset(set2)) #False
# print(set1.issuperset(set2)) #False
# print(set1.union(set2)) #{0, 1, 2, 3, 4, 5, 7, 9}


### ==================================


# ## 딕셔너리

# person = {'name':'Alice' , 'age' : 25}

# # 1) .clear() -> 딕셔너리 요소 싹 다 제거

# person.clear()

# print(person) #{}

# # 2) .get(key[,default])

# print(person.get('name')) #Alice

# print(person.get('country')) #None

# print(person.get('country','해당 키가 없습니다.')) #None이 아니라 '해당 키가 없습니다.'이 나옴!

# # key in dict != dict.get(key)

# # 3) .keys()

# print(person.keys()) # dict_keys(['name', 'age']) -> 우리가 아예 본 적 없는 데이터 타입.
# #근데 '대괄호로 묶여 있다'라는 점에 집중 => 1. key의 모임 2. 대괄호로 묶여있다면 반복이 가능한 객체(iterable) 이란걸 생각 -> 굳이 데이터 타입을 안 바꿔도 iterable한 곳에 넣을 수 있다!

# # 4) .values() -> 키에 접근하지 않아도 value에 접근할 수 o

# print(person.values()) # dict_values(['Alice', 25] -> 이것도 대괄호로 묶임
# #1. value의 모임 2. iterable

# # 5) .items() -> 키와 값 둘 다 쌍을 뽑는거 tuple형태로!

# print(person.items()) #dict_items([('name', 'Alice'), ('age', 25)])
# #1. key와 value의 튜플로 묶인 모임 2. 쌍으로 나오는 iterable 

# # for key, value in person.items(): #-> 언패킹
# #     print(key,value) 
#     #name Alice
#     #age 25

# # 6) .pop(key[,default])

# print(person.pop('name')) #Alice
# print(person) #{'age': 25}
# print(person.pop('country')) #KeyError: 'country'
# print(person.pop('country','해당 키는 존재하지 않습니다.')) #해당 키는 존재하지 않습니다.


# # 7) setdefault : set default -> 기본 값을 할당한다. .get과 비슷한데, 만약 키가 없으면 *딕셔너리에 추가*

# print(person.setdefault('country','korea')) #korea

# print(person) #{'name': 'Alice', 'age': 25, 'country': 'korea'}

# # 8) .update([other]) -요소를 딕셔너리에 넣기

# other_person ={
#     'name' : 'Jane',
#     'Gender' : "Female"
# }

# person.update(other_person)

# print(person) #{'name': 'Jane', 'age': 25, 'country': 'korea', 'Gender': 'Female'}

# person.update(age=50)
# print(person) #{'name': 'Jane', 'age': 50, 'country': 'korea', 'Gender': 'Female'}

#==============================================================================

# # # 01-23 실습

# my_dict = {
#     'plust' : ['더하기','빼기'],
#     'minus' : ["빼기", '적자'],
#     'multiply' : ['곱하기','다양하게'],
#     'division' : ['나누기','분열']      
# }

# # #실습 1. '빼기' 반환(4가지)

# print(my_dict['plust'][1])

# print(my_dict.get('minus'))[0]

# print(my_dict.setdefault('minus')[0])

# print(my_dict.pop('minus')[0])

# #실습 2. key값 순차적으로 출력(for문 사용)

# keys = my_dict.keys()

# for i in keys:
#     print(i) 

# #####
# for i in my_dict.keys():
#     print(i)

# #####
# # 딕셔너리는 반복문 돌리면 자동으로 key값이 돈다

# for key in my_dict:
#     print(key)
 
# # 실습 3. 'square' : ['제곱','사각형'] 추가(4가지 방법)
    
# #1) setdefault
    
# my_dict.setdefault('square',['제곱','사각형'])
# print(my_dict)

# #2) update

# my_dict.update(square=['제곱','사각형']) #여기서 key에 '' 넣으면 안됨
# print(my_dict)

# #3) update

# other = {'square':['제곱','사각형']}
# my_dict.update(other)
# print(my_dict)

# #4) update

# my_dict.update({'square':['제곱','사각형']})
# print(my_dict)

# #5) 메서드 사용 안 하고 -직접 할당

# my_dict['square'] = ['제곱','사각형']
# print(my_dict)

# # #실습 4. 'division' 제거 (2가지 방법)

# #1) pop

# my_dict.pop('division')
# print(my_dict)

# #2) del

# del(my_dict['division'])
# print(my_dict)


#==========================================

# print(hash(1))
# print(hash(2))
# print(hash('a'))
# print(hash('b'))


my_set = {39, 5, 1, 4, 3, 9, 10, 2, 100, 52}

print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set)
