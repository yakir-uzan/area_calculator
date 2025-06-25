from calculator import Shape
import math

class Circle(Shape):
    def _init_(self, radius):
        super()._init_(name = "circle")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def _str_(self):
        return f"{self.name} (radius={self.radius}) with area: {self.get_area():.2f}"