class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self,lenght):
        Shape.__init__(self)
        self.lenght = lenght
    def area(self):
        return self.lenght * self.lenght
    
sq = Square(int(input()))
print(sq.area())

    