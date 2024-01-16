#============================================

#<단축>

# print(bool(0))
# print(bool(1))
# print(bool(5))
# print(bool(-1))

# print(bool(''))  #False
# print(bool('t')) #True
# print(bool('false'))  #True
# print(bool('True'))   #True
# print(bool('False'))  #True
# print(bool(False))    #False

# print('a' and 'b')  #b
# print('b' and 'a')  #a
# print('a' or 'b')   #a
# print('b' or 'a')   #b
# print('' or 'a')    #a
# print('' and 'a')   #결과값 ''라서 아무것도 안 나옴
# print(False and 'a') #False

# print('a' or 'b' and False)     #a
# print(('a' or 'b') and False)   #False

#======================================
#<복합연산자>
# a=list(range(11))
# print(sum(a))
# sum_value=0
# for i in range(11):
#     sum_value += i

# print(sum_value)


#===================================================

#<명시적 형변환>


# n=input()
# print(type(n))      #input()은 무조건 str

#-로또 6번호 추첨

#======================================================


#<Sequence Type>


#list

# 가변 sequence 자료형 -> 순서o -> 인덱싱, 슬라이싱, 길이, 반복 가능


# MAP = []

# Matrix = []

# array = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]

# #실습 1 인덱싱하여 3을 출력해보세요.

# print(array[0][2])

# #실습 2 인덱싱하여 7을 출력해보세요.

# print(array[2][0])

# #실습 3 슬라이싱하여 [2, 3]을 출력해보세요.

# print(array[0][1:3])

# # 실습 3-1 슬라이싱하여 2 3을 출력해보세요.

# print(*array[0][1:3]) #unpacking

