# Write a Python Program to demonstrate the different types of constructors
# Default Constructor
class default_Constructor:
    # default constructor
    def __init__(self):
        self.str1 = "Welcome to Python Programming"

    # a method for printing data members
    def print_Message(self):
        print(self.str1)


# creating object of the class
obj = default_Constructor()
# calling the instance method using the object obj
obj.print_Message()

# Parameterised Constructor
class Rectangle_Area:
    length = 0
    breath = 0
    area = 0

    # parameterized constructor
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def display(self):
        print("Length= " + str(self.length))
        print("Breadth = " + str(self.breadth))
        print("Area of rectangle= " + str(self.area))

    def calc_area(self):
        self.area = self.length * self.breadth

# creating object of the class invoking parameterized constructor
obj = Rectangle_Area(10, 20)
# compute Area
obj.calc_area()
# display result
obj.display()
