# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        try :
            self.name = input('이름을 입력하세요 : ')
            self.age = int(input('나이를 입력하세요 : '))
            #메서드는 기존 LEGB 룰의 지역변수, 전역변수와 다르게 self에 제대로 할당이 된다.
            self.user_data['이름'] = self.name
            self.user_data['나이'] = self.age
            #user_data 딕셔너리에 데이터 삽입
            
        except ValueError:
            print('나이는 숫자로 입력해야 합니다.')
            
    # def display_user_info(self):
    #     try:
    #         print(f'이름 : {self.name}\n나이 : {self.age}')

    #     except AttributeError:
    #         print('사용자 정보가 입력되지 않았습니다.')

    
    def display_user_info(self):
            if self.user_data: #user_data에 뭐라도 들어가있으면 True
                for key, value in self.user_data.items():
                    print(f'{key} : {value}')
            else:
                print('사용자 정보가 입력되지 않았습니다.')


user = UserInfo()
user.get_user_info()
user.display_user_info()
