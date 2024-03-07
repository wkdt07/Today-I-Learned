# 아래에 코드를 작성하시오.

class Myth:
    type_of_myth = 0
    
    def __init__(self,name):
        self.name = name
        # type_of_myth += 1
        Myth.type_of_myth += 1 #클래스 변수 끌고 오기, 48p 확인
        #init 매서드에서 클래스 변수에 접근하려면 클래스명.클래스변수명 으로 접근해야한다. (init 매서드 특징)

        #인스턴스 매서드의 경우 self.type_of_myth += 1 , 클래스 매서드의 경우 cls.type_of_myth += 1 로 접근한다.
        #인스턴스의 속성 default는 class에서 갖고 오는거, 만약 self.type_of_myth가 따로 지정이 되어 있지 않다면 그 값이 class의 값으로 default됨. 그래서 이런 식으로 한 번 선언하고 가는거
    

    @staticmethod
    def description():
        print('신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')
        # Myth.type_of_myth += 1 , 만약 여기에 넣고 싶다면 static은 별개의 공간이므로 이런 식으로 갖고 와야함



dangun = Myth('dangun')
greek_rome = Myth('greek & rome')

print(dangun.name)
print(greek_rome.name)
print(f'현재까지 생성된 신화 수:{Myth.type_of_myth}')
Myth.description()
print(Myth.type_of_myth)

