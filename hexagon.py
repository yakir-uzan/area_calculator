from calculator import Shape
import math

class Hexagon(Shape):
    def __init__(self, side_length):
        super().__init__(name = "Hexagon")
        self.side_length = side_length
        self.sides = [side_length] * 6

    def get_area(self):
        return (3 * math.sqrt(3) / 2) * (self.side_length ** 2)

    def get_perimeter(self):
        return 6 * self.side_length

    def __str__(self):
        return f"{self.name} (side_length = {self.side_length}) \narea: {self.get_area():.2f}, \nperimeter: {self.get_perimeter():.2f}"

