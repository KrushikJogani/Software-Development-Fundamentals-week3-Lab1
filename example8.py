# Example 8: Count down from a number to 1

num = int(input("Enter a number to count down from: "))  # getting number from user

while num > 0:       # looping until it reaches 0
    print(num)
    num -= 1         # decreasing by 1 each time

print("Done!")