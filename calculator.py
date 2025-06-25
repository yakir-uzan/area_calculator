from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name = "Shape"):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

    def __str__(self):
        return f"{self.name} with area: {self.get_area()}"

    #מתודת קסם שמחברת בין 2 צורות
    def __add__(self,other):
        if isinstance(other,Shape):
            return self.get_area() + other.get_area()
        return NotImplemented

    #מתודת קסם שמשווה בין 2 צורות
    def __eq__(self, other):
        if isinstance(other, Shape):
            return self.get_area() == other.get_area()
        return NotImplemented