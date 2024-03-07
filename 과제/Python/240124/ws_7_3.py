# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self,a,b):
        self.width = a
        self.height = b
    
    def calculate_area(self):
        area = self.width * self.height
        return area
    
    def calculate_perimeter(self):
        result = 2 * (self.width + self.height)
        return result

shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)


'''
<인스턴스 메서드의 변수>
인스턴스가 만들어지면 init에 의해 속성(width, height)이 정해진다.

shape1 = Shape(5, 3)
shape1.calculate_perimeter()

의 경우

흐름이 shape1 생성, 동시에 shape1의 속성이 결정.
그 속성을 토대로 calculate_perimeter가 평가된다.
shape1.calculate_perimeter() == calculate(shape1)
여기서 shape1의 width, height 가 shape1에 묶여서 통으로 들어가게 되므로
우리가 따로 이를 선언하지 않고

함수에서 result = 2 * (self.width + self.height) 이런 식으로 바로 사용하는 것이다.
'''