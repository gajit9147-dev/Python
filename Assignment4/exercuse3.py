with open("numbers.txt","w") as file:
    file.write("1\n2\n3\n4\n5")

with open("numbers.txt", "r") as file:
    content = file.read()
    print(content)
