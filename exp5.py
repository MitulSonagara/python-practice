def first_and_last_same(numbers):
    if len(numbers) < 2:
        return False  # If the list has less than 2 elements, they cannot be the same
    return numbers[0] == numbers[-1]

# Example usage:
num_list = [1, 2, 3, 4, 5, 1]
result = first_and_last_same(num_list)
print("First and last elements are the same:", result)
