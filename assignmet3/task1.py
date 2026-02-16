num = input("Enter a non-negative integer: ")

try:
    n = int(num)
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")
else:
    if n < 0:
        print("Invalid input. Please enter a non-negative integer.")
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        print(f"The factorial of {n} is {factorial}")
