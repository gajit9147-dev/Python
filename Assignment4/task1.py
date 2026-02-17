file_name = "sample.txt"

try:
    print("Reading file content:\n")
    
    with open(file_name, "r") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")