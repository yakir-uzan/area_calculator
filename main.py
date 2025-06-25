from circle import Circle
from hexagon import Hexagon
from rectangle import Rectangle
from square import Square
from triangle import Triangle


def main():
    # מימוש מלבן
    rect = Rectangle(5, 10)
    print(rect)

    #מימוש ריבוע
    squa = Square(4)
    print(squa)

    #מימוש משולש
    trian = Triangle(3,5)
    print(trian)

    #מימוש עיגול
    circ = Circle(6)
    print(circ)

    #מימוש משושה
    hexa = Hexagon(7)
    print(hexa)

    #מימוש חיבור בין 2 צורות
    print(trian + circ)

    #מימוש השוואה בין 2 צורות
    print(squa == trian)


if __name__ == "__main__":
    main()
