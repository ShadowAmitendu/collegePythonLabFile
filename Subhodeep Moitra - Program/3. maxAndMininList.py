def find_max_min(lst):
    maximum = lst[0]
    minimum = lst[0]
    for element in lst:
        if element > maximum:
            maximum = element
        if element < minimum:
            minimum = element
    return maximum, minimum


# Taking input
n = int(input("Enter number of elements in the list: "))
user_list = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]
max_element, min_element = find_max_min(user_list)
print(f"Maximum element: {max_element}")
print(f"Minimum element: {min_element}")
