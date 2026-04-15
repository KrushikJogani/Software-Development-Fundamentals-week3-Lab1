# Example 9: Find the maximum of three numbers

def find_max(a, b, c):  # function to find the max value
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = int(input("Enter first number: "))   # getting first number
num2 = int(input("Enter second number: "))  # getting second number
num3 = int(input("Enter third number: "))   # getting third number

print("Maximum:", find_max(num1, num2, num3))  # printing the max value