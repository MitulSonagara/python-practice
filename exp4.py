def remove_characters(string, n):
    if n >= len(string):
        return ""  # Return an empty string if n is greater than or equal to the string length
    else:
        return string[n:]

# Example usage:
input_string = input("Enter a string: ")
n = int(input("Enter the index to remove characters up to: "))

new_string = remove_characters(input_string, n)
print("New string:", new_string)
