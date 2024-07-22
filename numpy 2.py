""" 2. Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.

 Input: my_list = [1, 2, 3, 4, 5]"""

import numpy as np

# Given list
my_list = [1, 2, 3, 4, 5]

# Convert list to numpy array
my_array = np.array(my_list)

# Display the array
print("Array:", my_array)

# Display the first and last index
print("First index:", my_array[0])
print("Last index:", my_array[-1])

# Multiply each element by 2
multiplied_array = my_array * 2

# Display the result
print("Multiplied array:", multiplied_array)

""" output
Array: [1 2 3 4 5]
First index: 1
Last index: 5
Multiplied array: [ 2  4  6  8 10]
"""
