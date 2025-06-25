from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Squade"

    def __str__(self):
        return f"{self.name} (side = {self.side}) with area: {self.get_area():.2f}, perimeter: {self.get_perimeter():.2f}"
