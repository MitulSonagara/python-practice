my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_delete = {'b', 'd'}

for key in keys_to_delete:
    my_dict.pop(key, None)

print("Updated dictionary:", my_dict)
