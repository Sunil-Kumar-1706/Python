#Log Session a Shape base class with an area() method, then implement it differently in Circle and Square.

import math
class shape:
    def area():
        print("AREA")
class circle(shape):
    def area(self,r):
        return math.pi*r**2
class square(shape):
    def area(self,s):
        return s*s

c=circle()
print(round(c.area(2),2))
s=square()
print(s.area(2))
           