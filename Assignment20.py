""" 20. Write a Python program to get the key, value and item in a dictionary.
input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
Output:
key  value
1         10
2        20
3       30
4       40
5       50
6      60  """

# Input dictionary
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Print header
print("key", "value")

# Iterate through the dictionary and print key-value pairs
for key, value in dict_num.items():
    print(key, "\t", value)

#output
""" key value
1 	 10
2 	 20
3 	 30
4 	 40
5 	 50
6 	 60
"""
