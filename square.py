from rectangle import Rectangle

class Square(Rectangle):
    def _init_(self, side):
        super()._init_(side, side)
        self.name = "Squade"