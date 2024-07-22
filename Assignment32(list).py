#2. Write a Python program to get the largest and smallest number from a list without builtin functions.

def find_largest_and_smallest(numbers):
    if len(numbers) == 0:
        return None, None  # Return None if the list is empty

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    return largest, smallest

# Example usage
example_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
largest, smallest = find_largest_and_smallest(example_list)
print("Largest number in the list is:", largest)
print("Smallest number in the list is:", smallest)



"""output
Largest number in the list is: 9
Smallest number in the list is: 1"""
