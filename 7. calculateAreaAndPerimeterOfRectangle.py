# Write a python program to calculate area and perimeter of a rectangle.

length = float(input("ENTER THE LENGTH: "))
breadth = float(input("ENTER THE BREADTH: "))

area = length * breadth
peri = 2 * (length + breadth)

print("THE AREA AND PERIMETER OF RECTANGLE IS: ")
print(f"THE AREA: {area}\nTHE PERIMETER: {peri}")
