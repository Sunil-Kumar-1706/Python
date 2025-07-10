#Log Session a Shape class with a method called draw(). Inherit and customize in Circle and Square.

class shape:
    def draw(self):
        print("Drawing Shape")

class circle(shape):
    def draw(self):
       print("Drawing Circle")

class square(shape):
    def draw(self):
        print("Drawing Square")

c=circle()
s=square()
c.draw()
s.draw()