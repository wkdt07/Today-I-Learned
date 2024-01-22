
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


a=['b','a','n','a','n']

# 1. 리스트 a의 마지막에 'a' 추가하기

a.append('a')
print(a)

# 2. 

# #2-1. 리스트 a를 오름차순으로 정렬 -> 원본 변경
# a.sort()
# print(a)

#2-2. 리스트 a를 오름차순으로 정렬 -> 원본 변경하지 않는다
# print(sorted(a))
b = a[:]
b.sort()
print(b)
print(a)

# 3. 리스트 a를 내림차순으로 정렬
b = a
b.sort(reverse=True)
print(b)

# 4. 리스트 a를 역순으로 뒤집기
a.reverse()
print(a)

# 5. 리스트 a에서 문자 'a'를 삭제하기
for i in range(a.count('a')):
    a.remove('a')
print(a)


#========================================

# 6. 리스트 a의 마지막 요소를 꺼내서 삭제하고 반환값 출력

b = a.pop()
print(b)
# 7. 리스트 a에서 문자 'n'의 갯수 출력
print(a.count('a'))