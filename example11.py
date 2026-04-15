# Example 11: Swap two elements in a list using comma assignment

my_list = [23, 65, 19, 90]  # defining the list

pos1 = int(input("Enter position 1: ")) - 1  # getting first position (minus 1 for index)
pos2 = int(input("Enter position 2: ")) - 1  # getting second position (minus 1 for index)

my_list[pos1], my_list[pos2] = my_list[pos2], my_list[pos1]  # swapping the two elements

print("List after swap:", my_list)  # printing the updated list