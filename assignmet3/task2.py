import math


num = input("Enter a number: ")

try:
	value = float(num)
except ValueError:
	print("Invalid input. Please enter a valid number.")
else:
	if value < 0:
		print("Square root and natural logarithm require a non-negative number.")
	elif value == 0:
		print("Square root:", math.sqrt(value))
		print("Natural logarithm: undefined for 0")
		print("Sine (radians):", math.sin(value))
	else:
		print("Square root:", math.sqrt(value))
		print("Natural logarithm:", math.log(value))
		print("Sine (radians):", math.sin(value))
