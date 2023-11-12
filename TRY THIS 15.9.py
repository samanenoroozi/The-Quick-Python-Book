'''Modify the Rectangle class’s code to make the dimension variables private.'''

class Rectangle:
    def __init__(self):
        self.__width = 2
        self.__height = 7

    def area(self):
        return (self.__width+self.__height)*2


rectangle = Rectangle()
print(rectangle.area())
