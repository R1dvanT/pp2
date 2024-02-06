class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def show(self):
        return self.x , self.y
    
    def move(self,a,b):
        self.x += a
        self.y += b
        return self.x , self.y
    
    def dist(self,c,d):
        dx = self.x - c
        dy = self.y - d
        s = (dx**2 + dy**2)
        return s**0.5
    
x = int(input())
y = int(input())
p = Point(x, y)
print(p.show())
print(p.move(int(input()), int(input())))
print(p.dist(int(input()), int(input())))



