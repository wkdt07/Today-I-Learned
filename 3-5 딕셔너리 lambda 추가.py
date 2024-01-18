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

info = create_user(name,age,address)

how_many_rental_list=list(map(lambda x : x//10,info['user_age']))

print(how_many_rental_list)