from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def create_shape(shape_class):
    if shape_class == Rectangle:
        width = get_positive_float("Enter width: ")
        height = get_positive_float("Enter height: ")
        return Rectangle(width, height)
    elif shape_class == Square:
        side = get_positive_float("Enter side length: ")
        return Square(side)
    elif shape_class == Triangle:
        base = get_positive_float("Enter base: ")
        height = get_positive_float("Enter height: ")
        side1 = get_positive_float("side1: ")
        return Triangle(base, height, side1)
    elif shape_class == Circle:
        radius = get_positive_float("Enter radius: ")
        return Circle(radius)
    elif shape_class == Hexagon:
        side = get_positive_float("Enter side length: ")
        return Hexagon(side)

def add_shapes(shape_class, name):
    print(f"\nAdding two {name}s:")
    print("Shape A:")
    a = create_shape(shape_class)
    print("Shape B:")
    b = create_shape(shape_class)
    result = a + b
    print("Result:", result)

def compare_shapes(shape_class, name):
    print(f"\nComparing two {name}s:")
    print("Shape A:")
    a = create_shape(shape_class)
    print("Shape B:")
    b = create_shape(shape_class)
    print("Equal:", a == b)
    print()

def show_menu():
    print()
    print("Shape Calculator - Choose an option:")
    while True:
        print( "\n== Menu ==")
        print("1. Rectangle - Area & Perimeter")
        print("2. Square - Area & Perimeter")
        print("3. Triangle - Area & Perimeter")
        print("4. Circle - Area & Perimeter")
        print("5. Hexagon - Area & Perimeter")
        print("6. Add two shapes")
        print("7. Compare two shapes")
        print("8. Exit")
        print()
        choice = input("Select an option: ")

        if choice == "1":
            shape = create_shape(Rectangle)
            print()
            print(shape)

        elif choice == "2":
            shape = create_shape(Square)
            print()
            print(shape)

        elif choice == "3":
            shape = create_shape(Triangle)
            print()
            print(shape)

        elif choice == "4":
            shape = create_shape(Circle)
            print()
            print(shape)

        elif choice == "5":
            shape = create_shape(Hexagon)
            print()
            print(shape)

        elif choice == "6":
            print("\nSelect shape to add:")
            print("1. Rectangle")
            print("2. Square")
            print("3. Triangle")
            print("4. Circle")
            print("5. Hexagon")
            sub_choice = input(">> ")

            classes = {
                "1": (Rectangle, "Rectangle"),
                "2": (Square, "Square"),
                "3": (Triangle, "Triangle"),
                "4": (Circle, "Circle"),
                "5": (Hexagon, "Hexagon")
            }

            if sub_choice in classes:
                cls, name = classes[sub_choice]
                add_shapes(cls, name)
            else:
                print("Invalid shape selection.")

        elif choice == "7":
            print("\nSelect shape to compare:")
            print("1. Rectangle")
            print("2. Square")
            print("3. Triangle")
            print("4. Circle")
            print("5. Hexagon")
            sub_choice = input(">> ")

            classes = {
                "1": (Rectangle, "Rectangle"),
                "2": (Square, "Square"),
                "3": (Triangle, "Triangle"),
                "4": (Circle, "Circle"),
                "5": (Hexagon, "Hexagon")
            }

            if sub_choice in classes:
                cls, name = classes[sub_choice]
                compare_shapes(cls, name)
            else:
                print("Invalid shape selection.")

        elif choice == "8":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Please try again.")
