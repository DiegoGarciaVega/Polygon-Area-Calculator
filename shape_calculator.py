class Rectangle(object):
  #Attributes
  width = 0
  height = 0
  def __init__(self, width, height):
    self.height = height
    self.width = width

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height
  
  def get_area(self):
    return self.width*self.height
    
  def get_perimeter(self):
    return ((self.height + self.width) * 2)

  def get_diagonal(self):
    return (((self.width ** 2 + self.height ** 2) ** .5))

  def get_picture(self):
    if (self.width > 50 or self.height > 50):
      return "Too big for picture."
    aux = ""
    for i in range(self.height):
      aux += "*" * self.width
      aux += "\n"
    return aux
    
  def get_amount_inside(self,obj):  
    return self.get_area() // obj.get_area()

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

#Inherit from  Rectangle
class Square(Rectangle):
  def __init__(self,side):
    self.height = side
    self.width = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, side):
    self.width = side
    self.height = side

  def set_height(self, side):
    self.height = side
    self.width = side
  
  def __str__(self):
    return "Square(side=" + str(self.width) + ")"