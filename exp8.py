def is_palindrome(number):
    return str(number) == str(number)[::-1]

num = "naman"  # Replace with the number you want to check
result = is_palindrome(num)
print("Is it a palindrome?", result)
