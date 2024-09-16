def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


n = int(input("Enter number of elements in the list: "))
user_list = sorted([int(input(f"Enter element {i + 1}: ")) for i in range(n)])
target = int(input("Enter the element to search for: "))

if binary_search(user_list, target):
    print(f"{target} is found in the list.")
else:
    print(f"{target} is not found in the list.")
