import math
#part 1

gcd = math.gcd(48,180)
print(f"greatest common divisor : {gcd}")

sine_90 = math.sin(math.radians(90))
cos_60 = math.cos(math.radians(60))
tan_45 = math.tan(math.radians(45))
convert = math.radians(180)

print("Sine 90 = {:.2f}, \nCosine 60 = {:.2f}, \nTan 45 = {:.2f}, \nConvert = {:.2f}".format(sine_90,cos_60,tan_45,convert))


#part 2
nl_20 = math.log10(20)
l_10 = math.log10(1000)
expo = math.exp(3)
print("natural logarithm of 20 : {:.1f}\nbase-10 logarithm of 1000 : {:.2f}\ne^3 : {:.2f}".format(nl_20,l_10,expo))

#part 3

print("rounding off 7.856: {:.2f}".format(7.856))
floor = math.floor(12.78)
ceiling = math.ceil(12.78)
abs = abs(-45.6)

print("Floor value: {}\nCeiling value: {}\nAbsolute: {}".format(floor,ceiling,abs))

#part 4
print("Pi = {} \ne = {}".format(math.pi,math.e))
area = math.pi * pow(7,2)
print(f"Area = {area}")

#part 5
fact = math.factorial(7)
den = math.factorial(3) * math.factorial(7)

nCr = math.factorial(10) / den 
p = 3**2 + 4**2
hypo = math.sqrt(p)
d = 9.8*pow(5,2)/2

print("factorial : {}\n10C3 : {}\nhypotenuse : {}\nDistance: {}".format(fact,nCr,hypo,d))

print()