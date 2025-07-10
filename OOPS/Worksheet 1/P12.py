#Log Session a Calculator class with methods for add, subtract, multiply, and divide.

class calc:
    def __init__(self,x,y):
        self.x,self.y=x,y

    def add(self):
        return self.x+self.y
    
    def sub(self):
        return self.x-self.y
    
    def mul(self):
        return self.x*self.y
    
    def div(self):
        return self.x//self.y
    
x=calc(5,4)
y=calc(10,2)
print(x.add(),y.div())