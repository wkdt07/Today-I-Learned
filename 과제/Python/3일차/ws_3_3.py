# def rental_book(name,how_many_rental):
#     decrease_book(how_many_rental)
#     number = how_many_rental
#     print(f'{name}님이 {number}권의 책을 대여하였습니다')

    

# number_of_book = 100
# how_many_rental = int(input())

# def decrease_book(how_many_rental):
#     global number_of_book
#     number_of_book -= how_many_rental
#     return number_of_book
# #인자를 안 받아서 global로 놓긴 했는데 꼭 써야 하나?
# #여기서 함수 실행하자마자 print 해야하는건지를 모르겠다. 위에서 return값 쓸 거 생각하면 이게 맞는거 같기도 하고

# print(f'남은 책의 수 : {decrease_book(how_many_rental)}')
# rental_book('홍길동',how_many_rental)



def rental_book(name,how_many_rental):
    decrease_book(how_many_rental) #이러면 rental 함수 사용하면 decrease 까지 출력
    number = how_many_rental
    print(f'{name}님이 {number}권의 책을 대여하였습니다')

    

number_of_book = 100
how_many_rental = int(input())

def decrease_book(how_many_rental):
    global number_of_book
    number_of_book -= how_many_rental
    print(f'남은 책의 수 : {number_of_book}')

rental_book('홍길동',how_many_rental)