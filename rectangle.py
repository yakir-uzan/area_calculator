from calculator import Shape

class Rectangle(Shape):
    def _init_(self, width, height):
        super()._init_(name = "Rectangle")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def _str_(self):
        return f"{self.name} (width={self.width}, height={self.height}) with area: {self.get_area()}"