import math
class shape:
    def area(self):
      raise NotImplementedError("subclasses must override area()")  
    
class Rectangle(shape):
   def __init__(self, length, width):
      self.length = length
      self.width =width

class circle(shape):
   def __init__(self, radius):
      self.radius =radius
def area(self):
   return (f"Rectangle {self.length }* {self.width}")
       
def area(self):
   return math.pi *self.radius **2
