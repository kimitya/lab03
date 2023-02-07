class firstClass:
    def getString(self):
        self.input = input()
    
    def printString(self):
        print(self.input.upper())

x = firstClass()
x.getString()
x.printString()