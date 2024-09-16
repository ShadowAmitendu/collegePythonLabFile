def is_palindrome(num):
    original_num = num
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num //= 10
    return original_num == reversed_num


# Taking input
number = int(input("Enter an integer: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
