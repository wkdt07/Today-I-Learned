number_of_people = 0


def increase_user():
    pass


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name,age,address):
    info = {
        'user_name' : name,
        'user_age' : age,
        'user_address' : address
    }
        
    return info


many_user = list(map(create_user,name,age,address))


def rental_book(info):
    info = many_user
    decrease_book(how_many_rental) #이러면 rental 함수 사용하면 decrease 까지 출력
    number = how_many_rental
    print(f'{name}님이 {number}권의 책을 대여하였습니다')

    

number_of_book = 100
how_many_rental = list(map(lambda x : x/10,age,))

def decrease_book(*how_many_rental):
    global number_of_book
    number_of_book -= how_many_rental
    print(f'남은 책의 수 : {number_of_book}')


rental_book(create_user(name,age,address))