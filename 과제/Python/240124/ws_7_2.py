# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self,a,b):
        self.width = a
        self.height = b
    
    def calculate_area(self):
        area = self.width * self.height
        return area


shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)
