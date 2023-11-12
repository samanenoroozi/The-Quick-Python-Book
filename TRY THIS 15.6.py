'''Rewrite the code for a Rectangle class to inherit
from Shape. Because squares and rectangles are related, would it make sense
to inherit one from the other? If so, which would be the base class, and which
would inherit?'''


class Shape:
    def __init__(self, x, y):
       self.x = x
       self.y = y
       
class Rectangle(Shape):
    def __init__(self, x, y):
        Shape.__init__(self, x, y)
        
    def area(self):
        return self.x * self.y
   
class Square(Rectangle):
    def __init__(self, x):
        Shape.__init__(self, x, x)
    
r1=Rectangle(7,7)#square
r2=Rectangle(7,8)
s1=Square(11)
print(r1.area())
print(r2.area())
print(s1.area())


'''Should the area method be moved into the base Shape class and inherited by circle, square, and rectangle? If so, what issues would result?
'''

class Shape:
    def __init__(self, x, y):
       self.x = x
       self.y = y
    def area(self):
        return self.x*self.y
    
class Rectangle(Shape):
    pass

class Square(Rectangle):
    def __init__(self, x):
        Shape.__init__(self, x, x)
    
s1=Square(13)
r2=Rectangle(3,5)
print(s1.area())
print(r2.area())
