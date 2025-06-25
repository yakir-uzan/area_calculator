from circle import Circle
from hexagon import Hexagon
from rectangle import Rectangle
from square import Square
from triangle import Triangle
from menu import show_menu


def main():
    # מימוש מלבן
    rect = Rectangle(5, 5)

    #מימוש ריבוע
    squa = Square(5)

    #מימוש משולש
    trian = Triangle(3,5,5)

    #מימוש עיגול
    circ = Circle(6)

    #מימוש משושה
    hexa = Hexagon(7)



if __name__ == "__main__":
    show_menu()
    main()
