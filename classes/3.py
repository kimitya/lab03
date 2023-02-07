class Shape:
    def Area():
        return 0

class Rectangle (Shape):
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width
    
    def Area(self):
        return self.length*self.width
    
s=Rectangle(int(input("Rectangle's length: ")), int(input("Rectangle's width: ")))
print(s.Area())    
        
        