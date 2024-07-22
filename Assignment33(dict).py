"""1. Write a Python program and calculate the mean of the below dictionary.

 test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}

 Output: 6.2"""

def calculate_mean(dictionary):
    total = 0
    count = 0
    for value in dictionary.values():
        total += value
        count += 1
    mean = total / count
    return mean

# Given dictionary
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Calculate the mean
mean_value = calculate_mean(test_dict)

# Print the mean value
print("The mean of the dictionary values is:", mean_value)

#output
#The mean of the dictionary values is: 6.2
