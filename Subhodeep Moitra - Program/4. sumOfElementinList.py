def sum_of_list(lst):
    total = 0
    for element in lst:
        total += element
    return total


# Taking input
n = int(input("Enter number of elements in the list: "))
user_list = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]
print("Sum of elements in the list:", sum_of_list(user_list))
