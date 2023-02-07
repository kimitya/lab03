from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)
    
    def move(self):
        self.x = int(input("New coordinate for x: "))
        self.y = int(input("New coordinates for y: "))
    
    def dist(self, x1, y1):
        return sqrt((self.x - x1)**2 + (self.y - y1)**2)

p = Point(1, 1)
p.move()
print(p.dist(2, 2))
print(p.dist(int(input()), int(input())))