# Write a Python program to sum all the items in a list.

def sum_list(items):
    total = 0
    for item in items:
        total += item
    return total

# Example usage
example_list = [1, 2, 3, 4, 5]
print("The sum of the list is:", sum_list(example_list))

#output
#The sum of the list is: 15
