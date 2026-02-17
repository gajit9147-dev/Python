# Program to read content from a file and print it

with open("myname.txt", "r") as file:
    content = file.read()
    print(content)

#Write a program to append a new line to an existing file.

with open("myname.txt", "a") as file:
    file.write("\n this is my first append operation in python.")
    print("Data successfully appended to myname.txt.")

