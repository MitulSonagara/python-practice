my_list = [1, 2, 3, 4, 5]
my_dict = {1: 'one', 3: 'three', 5: 'five', 7: 'seven'}

my_list = [x for x in my_list if x in my_dict.keys()]
print("Updated list:", my_list)
