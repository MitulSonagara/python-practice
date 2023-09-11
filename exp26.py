def append_in_middle(s1, s2):
    middle_index = len(s1) // 2
    return s1[:middle_index] + s2 + s1[middle_index:]

s1 = "Hello"
s2 = "World"
result = append_in_middle(s1, s2)
print("Result:", result)
