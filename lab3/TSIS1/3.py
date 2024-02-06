class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self,lenght,wet):
        Shape.__init__(self)
        self.lenght = lenght
        self.wet = wet
    def area(self):
        return self.lenght * self.wet

a = int(input())
b = int(input())
sq = Square(a, b)
print(sq.area())
