# Example 5: Accept full name and print in reverse order

name = input("Input your name: ")  # getting full name from user
parts = name.split()  # splitting name into first and last
print(parts[1], parts[0])  # printing last name then first name