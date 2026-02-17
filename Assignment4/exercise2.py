# Program to read content from a file and print it

with open("myname.txt", "r") as file:
    content = file.read()
    print(content)
