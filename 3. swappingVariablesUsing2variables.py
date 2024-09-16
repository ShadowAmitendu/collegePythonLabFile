# Write a python program to SWAP two numbers (without using 3rd variable).

a, b = 10, 255

print(f"BEFORE SWAPPING: {a, b}")

a = a + b
b = a - b
a = a - b

print(f"AFTER SWAPPING: {a, b}")
