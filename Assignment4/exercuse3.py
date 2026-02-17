with open("numbers.txt","w") as file:
    file.write("1\n2\n3\n4\n5")

with open("numbers.txt", "r") as file:
    content = file.read()
    print(content)

# Program to count total characters in a file

file_name = "numbers.txt"

with open(file_name, "r") as file:
    content = file.read()
    char_count = len(content)

print("Total number of characters in the file:", char_count)
