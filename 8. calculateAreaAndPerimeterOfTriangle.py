# Write a python program to calculate area and perimeter of a triangle where three sides are user given.
import math

side1 = float(input("ENTER THE SIDE 1: "))
side2 = float(input("ENTER THE SIDE 2: "))
side3 = float(input("ENTER THE SIDE 3: "))

peri = side1 * side2 * side3
semiPeri = peri / 2
sqrtArea = semiPeri * (semiPeri - side1) * (semiPeri - side2) * (semiPeri - side3)
area = math.sqrt(sqrtArea)

print("THE AREA AND PERIMETER OF TRIANGLE IS: ")
print(f"THE AREA: {area}\nTHE PERIMETER: {peri}")