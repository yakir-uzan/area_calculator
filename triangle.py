from rectangle import Rectangle

class Triangle(Rectangle):
    def _init_(self,base, height):
        super()._init_(base, height)
        self.name = "Triangle"

    def get_area(self):
        return 0.5 * self.width * self.height