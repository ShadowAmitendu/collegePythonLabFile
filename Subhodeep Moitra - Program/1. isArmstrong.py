def is_armstrong(num):
    sum_of_powers = 0
    digits = [int(d) for d in str(num)]
    num_digits = len(digits)
    for digit in digits:
        sum_of_powers += digit ** num_digits
    return sum_of_powers == num


# Taking input
number = int(input("Enter an integer: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
