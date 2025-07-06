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
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5

    def get_picture(self):
        pass

    def get_amount_inside(self):
        pass

class Square(Rectangle):
    pass

test = Rectangle()
test.set_width(4)
test.set_height(2)
print(test.get_diagonal())
