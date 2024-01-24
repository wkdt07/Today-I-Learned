
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
    
    def print_info(self):
        peimeter = self.calculate_perimeter()
        area = self.calculate_area()
        print(f'width: {self.width}\nheight: {self.height}\nArea: {area}\nPerimeter: {peimeter}')
        # 여러 함수를 def 하는 과정에서 이전에 def 했던 부분을 self를 넣어서 계산한 후, 그 값을 사용할 수도 있다.

    
shape1 = Shape(5, 3)
shape1.print_info()
