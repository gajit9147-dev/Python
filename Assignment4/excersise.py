
#Write a Python program to create a text file and write your name into it.



with open("task1.txt", "w") as file:
    file.write("This is my first task on file handling in python.")

    print("Data successfully written to task1.txt.")