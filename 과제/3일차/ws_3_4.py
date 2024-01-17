number_of_people = 0


def increase_user():
    pass


def create_user(name,age,address):

    user_info = {
        'user_name' : name,
        'user_age' : age,
        'user_address' : address
    }
        
    return user_info



name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

print(list(map(create_user,name,age,address)))

