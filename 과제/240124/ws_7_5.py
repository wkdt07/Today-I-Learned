class Shape:
    def __init__(self,a,b):
        self.width = a
        self.height = b

    def __str__(self):
        return f'Shape: width={self.width}, height={self.height}'
    # __str__은 print 할 때 '자동으로 호출되어' 해당 내용을 return해서 print하게 하는 메서드 
        

shape1 = Shape(5, 3)
print(shape1)
