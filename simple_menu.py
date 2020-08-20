def area_of_circle(radius):
    area = 3.14 * radius ** 2
    return area


def area_of_rectangle(length, breadth):
    area = length * breadth
    return area


def area_of_triangle(base, height):
    area = 0.5 * base * height
    return area


def area_of_trapezium(p1, p2, h1):
    area = 0.5 * (p1 + p2) * h1
    return area


def area_of_sphere(radius):
    area = 4 * 3.14 * radius ** 2
    return area


def area_of_cube(length):
    area = 6 * length ** 2
    return area


def area_of_cuboid(length, breadth, height):
    area = 2*length*breadth + 2*length*height + 2*breadth*height
    return area


def areas_menu():
    print("""
        1. area of circle
        2. area of rectangle
        3. area of triangle
        4. area of trapezium
        5. area of sphere
        6. area of cube
        7. area of cuboid
    """)

    while True:
        num = int(input("enter choice: "))

        if num == 0:
            choice = input("do you want to exit? [y/n] ")
            if choice == 'n':
                areas_menu()
            if choice == 'y':
                print("goodbye, see you later :)")
                return

        elif num == 1:
            print("---[area of circle calculator]---")
            radius = float(input("enter radius: "))
            print(f"the area of the circle is: {area_of_circle(radius)}")

        elif num == 2:
            print("---[area of rectangle calculator]---")
            length = float(input("enter length: "))
            breadth = float(input("enter length: "))
            print(f"the area of the rectangle is: {area_of_rectangle(length, breadth)}")

        elif num == 3:
            print("---[area of triangle calculator]---")
            base = float(input("enter base: "))
            height = float(input("enter height: "))
            print(f"the area of the triangle is: {area_of_triangle(base, height)}")

        elif num == 4:
            print("---[area of trapezium calculator]---")
            p1 = float(input("enter parallel side-1: "))
            p2 = float(input("enter parallel side-2: "))
            height_of_trapezium = float(input("enter height of trapezium: "))
            print(f"the area of the circle is: {area_of_trapezium(p1, p2, height_of_trapezium)}")

        elif num == 5:
            print("---[area of sphere calculator]---")
            radius = float(input("enter radius of sphere: "))
            print(f"area of sphere is: {area_of_sphere(radius)}")

        elif num == 6:
            print("---[area of cube calculator]---")
            length = float(input("enter length of cube: "))
            print(f"area of cube is: {area_of_cube(length)}")

        elif num == 7:
            print("---[area of cuboid calculator]---")
            length = float(input("enter length of cube: "))
            breadth = float(input("enter breadth of cube: "))
            height = float(input("enter height of cube: "))
            print(f"area of cuboid is: {area_of_cuboid(length, breadth, height)}")

        else:
            print("invalid choice!")
            choice = input("do you want to exit? [y/n] ")
            if choice == 'n':
                areas_menu()
            if choice == 'y':
                print("goodbye, see you later :)")
                return


areas_menu()