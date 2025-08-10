import math
class Shape:
    def area(self):
      raise NotImplementedError("subclasses must override area()")  
    
class Rectangle(Shape):
   def __init__(self, length, width):
      self.length = length
      self.width =width

class Circle(Shape):
   def __init__(self, radius):
      self.radius =radius
def area(self):
   return (f"Rectangle {self.length }* {self.width}")
       
def area(self):
   return math.pi *self.radius ** 2
