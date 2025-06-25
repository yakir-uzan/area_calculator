from calculator import Shape

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__(name = "Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.sides = [side1,side2,side3]

    def get_area(self):
        s = self.get_perimeter() / 2
        area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        return area

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return f"{self.name} (sides = {self.side1}, {self.side2}, {self.side3}) \narea: {self.get_area():.2f} \nperimeter: {self.get_perimeter():.2f}"
