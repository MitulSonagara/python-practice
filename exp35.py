list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

# Convert lists to dictionary
my_dict1 = dict(zip(list1, list2))

# Merge two dictionaries
my_dict2 = {'d': 4, 'e': 5}
merged_dict = {**my_dict1, **my_dict2}

print("Merged dictionary:", merged_dict)
