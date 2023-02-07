class Shape:
    def Area():
        return 0
        
class Square(Shape):
    def __init__ (self, length):
        self.length=length
    
    def Area(self):
        return self.length **2
    
k=Square(int(input("Square's length: ")))
print(k.Area())