class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def set_width(self, w):
        self.width = w
    
    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        pass

    def get_diagonal(self):
        pass

    def get_picture(self):
        pass

    def get_amount_inside(self):
        pass

class Square(Rectangle):
    pass

test = Rectangle()
test.set_width(4)
test.set_height(2)
print(test.get_area())
