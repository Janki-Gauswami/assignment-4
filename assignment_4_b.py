data = input("Enter text to write to the file: ")

with open("output.txt", "w") as f:
    f.write(data)

print("data successfully written to output.txt. /n")

a_data = input("Enter additional text to append: ")

with open("output.txt", "a") as f:
    f.write(a_data)

print("data successfully appended to output.txt. /n")

with open("output.txt") as f:
    print(f.read())