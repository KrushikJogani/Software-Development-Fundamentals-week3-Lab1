# Example 4: Calculate the perimeter and area of a rectangle

length = float(input("Enter length: "))  # getting length
width = float(input("Enter width: "))    # getting width

area = length * width            # calculating area
perimeter = 2 * (length + width) # calculating perimeter

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")