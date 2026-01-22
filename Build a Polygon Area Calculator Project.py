class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            picture = '*' * self.width + '\n'
            picture = picture * self.height
            return picture

    def get_amount_inside(self, object):
        return self.get_area() // object.get_area()

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.width = side
        Rectangle.height = side

    def set_side(self, side):
        Rectangle.width = side
        Rectangle.height = side

    def set_width(self, side):
        Rectangle.width = side
        Rectangle.height = side

    def set_height(self, side):
        Rectangle.height = side
        Rectangle.width = side

    def __str__(self):
        return f"Square(side={Rectangle.width})"


r1 = Rectangle(5, 10)
print(r1)
r1.set_width(10)
print(r1)

s1 = Square(10)
print(s1)
s1.set_side(14)
s1.set_height(20)
print(s1)