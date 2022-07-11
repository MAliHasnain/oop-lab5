class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        print("The area of given rectangle is : ",(self.width * self.height))

class Square(Rectangle):
    def __init__(self,width,height):
        super().__init__(width,height)
s = Square(4,4)
