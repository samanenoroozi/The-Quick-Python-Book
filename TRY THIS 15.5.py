#Write a class method similar to total_area() that returns the total circumference of all circles.

class Circle:
   all_circles = []
   pi = 3.14
   
   def __init__(self, r=5):
     self.radius = r
     Circle.all_circles.append(self)
   def circumference(self):
     return 2*Circle.pi * self.radius
   
   @classmethod
   def total_circumference(cls):
      total = 0
      for c in cls.all_circles:
          total = total + c.circumference()
      return total
   
c1 = Circle()
c2 = Circle(7)
c3 = Circle(11)
print(Circle.total_circumference())
