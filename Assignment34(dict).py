"""Write a Python script to concatenate the following dictionaries to create a new one. 

Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60}

 Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

def concatenate_dicts(*dicts):
    result = {}
    for dictionary in dicts:
        result.update(dictionary)
    return result

# Given dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate dictionaries
result_dict = concatenate_dicts(dic1, dic2, dic3)

# Print the result
print("Concatenated dictionary:", result_dict)


"""output
Concatenated dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""
