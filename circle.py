from calculator import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(name = "circle")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"{self.name} (radius = {self.radius}) with area: {self.get_area():.2f}"
