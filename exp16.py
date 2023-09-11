input_str = input("Enter three strings separated by spaces: ")
strings = input_str.split()
if len(strings) != 3:
    print("Please enter exactly three strings.")
else:
    str1, str2, str3 = strings
    print("You entered:", str1, str2, str3)
