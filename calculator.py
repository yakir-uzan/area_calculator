from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name = "Shape"):
        self.name = name
        self.sides = []

    """מתודה אבסטרקטית שמחזירה את שטח הצורה"""
    @abstractmethod
    def get_area(self):
        pass

    """מתודת קסם שמופעלת ברגע שעושים פרינט"""
    def __str__(self):
        return f"{self.name} area: {self.get_area()}"

    """מתודת קסם שמחברת בין 2 צורות"""
    def __add__(self,other):
        if isinstance(other,Shape):
            return self.get_area() + other.get_area()
        return NotImplemented

    """מתודת קסם שמשווה בין 2 צורות"""
    def __eq__(self, other):
        if isinstance(other, Shape):
            return self.get_area() == other.get_area()
        return NotImplemented

    """מתודה שבודקת אם צורה אחת קטנה מהשניה"""
    def __lt__(self, other):
        return self.get_area() < other.get_area()

    """מתודה שמחזירה את מספר הצלעות של הצורה"""
    def __len__(self):
        return len(self.sides)
