def square(a):
    a_square = a**2
    p_square = 2*a

    print(f"Area of square = {a_square} sq units, Perimeter of square = {p_square}")

def rectangle(c1,c2):
    a_rectangle = c1 * c2
    p_rectangle = 2*(c1 + c2)

    print(f"Area of rectangle = {a_rectangle} sq units, Perimeter of rectangle: {p_rectangle}")

def triangle(b):
    a_triangle = (3**0.5) * b / 2
    p_triangle = 3 * b

    print("Area of triangle = {:.2f} sq units, Perimeter of triangle = {}".format(a_triangle,p_triangle))



a = int(input("Enter the length of side of a square: "))
square(a)


b = int(input("Enter length of side of an equilateral triangle: "))
triangle(b)

c1 = eval(input("enter lenght of rectangle: "))  
c2 = eval(input("enter width of rectangle: "))
rectangle(c1,c2)
