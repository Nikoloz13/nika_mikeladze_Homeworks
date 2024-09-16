from math import sqrt 

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

perimeter = a + b + c

s = perimeter / 2

area = sqrt(s * (s - a) * (s - b) * (s - c))

perimeter_rounded = round(perimeter, 2)
area_rounded = round(area, 2)

print(f"The perimeter is: {perimeter_rounded} and The area is {area_rounded} ")