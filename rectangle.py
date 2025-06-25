from calculator import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(name = "Rectangle")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f"{self.name} (width = {self.width}, height = {self.height}) with area: {self.get_area()}"