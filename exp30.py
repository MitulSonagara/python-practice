num_list = [1, 2, 3, 2, 4, 3, 5, 6, 4]

count_dict = {}
for num in num_list:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

print("Count of each element:", count_dict)
