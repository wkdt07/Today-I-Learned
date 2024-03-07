number_of_people = 0



def increase_user():
    number_of_people=0
    number_of_people += 1
    return number_of_people



def create_user(name,age,address):
    user_info = {
        'user_name' : name,
        'user_age' : age,
        'user_address' : address
    }
        
    return user_info


print(f'현재 가입 된 유저 수 : {number_of_people}')
print(f"{create_user('홍길동','30','서울')['user_name']}님 환영합니다!")
print(create_user('홍길동','30','서울'))
print(f'현재 가입 된 유저 수 : {increase_user()}')