def combine_strings(s1, s2):
    result = s1[0] + s2[len(s2)//2] + s1[-1]
    return result

string1 = "abc"
string2 = "defg"
result = combine_strings(string1, string2)
print("Result:", result)
