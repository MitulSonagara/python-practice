previous_number = 0

for current_number in range(1, 11):
    current_sum = previous_number + current_number
    print(f"Current Number: {current_number}, Previous Number: {previous_number}, Sum: {current_sum}")
    previous_number = current_number
