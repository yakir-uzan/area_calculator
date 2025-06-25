from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"
        self.side = side
        self.sides = [side] * 4

    def __str__(self):
        return (f"{self.name} (side = {self.width}) \n"
                f"area: {self.get_area():.2f}, \n"
                f"perimeter: {self.get_perimeter():.2f}")