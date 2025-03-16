import math
import cmath
print("\nInput for num1")
a = int(input("enter real part= "))
b = int(input("enter imaginary part: "))
z1 = complex(a,b)

print("\nInput for num2")
c = int(input("enter real part= "))
d = int(input("enter imaginary part: "))
z2 = complex(c,d)


sum = z1 + z2
print("\nSum = ", sum)

diff = (z1-z2)
print("Difference = ", diff)

real_d =( a*c + b*d ) / (c**2 + d**2)
comp_d = (b*c - a*d) / (c**2 + d**2)
division = complex(real_d, comp_d)
print("Division z1/z2: ",division)

prod = complex(a*c - b*d, a*d + b*c)
print("Product: ",prod)
