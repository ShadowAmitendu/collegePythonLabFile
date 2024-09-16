# Write a python program to calculate area and perimeter of a circle.

PI = 3.14159

radius = float(input("ENTER THE RADIUS: "))

area = PI * (radius ** 2)
peri = 2 * PI * radius

print("THE AREA AND THE PERIMETER OF THE CIRCLE IS:: ")
print(f"PERIMETER: {peri}, \nAREA: {area}")
