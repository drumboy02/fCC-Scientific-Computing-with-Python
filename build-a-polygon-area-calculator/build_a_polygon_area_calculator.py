class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
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
        if self.height > 50:
            return 'Too big for picture.'
        line = ('*' * self.width + '\n')
        return line * self.height

    def get_amount_inside(self, shape):
        if type(shape) == Rectangle:
            return 'Rectangle'
            # area = self.get_area()
            # perimeter = self.get_perimeter()
        elif type(shape) == Square:
            return 'Square'
        return # (area, perimeter)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)
        self.side = side

    def __str__(self):
        return f'Square(side={self.side})'

    def set_side(self, s):
        self.side = s
        self.width = s
        self.height = s

test = Rectangle()
test.set_width(5)
test.set_height(10)
print(test.get_diagonal())
print(test.get_picture())
print(test.get_amount_inside(test))
sq = Square(2)
sq.set_side(4)
print(sq.get_amount_inside(sq))
print(sq.get_picture())
print(sq)