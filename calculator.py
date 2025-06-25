from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name = "Shape"):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

    def _str_(self):
        return f"{self.name} with area: {self.get_area()}"