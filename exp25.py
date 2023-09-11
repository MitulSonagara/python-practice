def middle_three_chars(s):
    middle_index = len(s) // 2
    return s[middle_index - 1:middle_index + 2]

input_string = "abcdefghidw"
result = middle_three_chars(input_string)
print("Middle three characters:", result)
