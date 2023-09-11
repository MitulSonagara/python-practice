def read_line_number(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if 1 <= line_number <= len(lines):
            return lines[line_number - 1]
        else:
            return "Line not found"

file_path = "input_file.txt"  # Replace with the path to your file
line_number = 4  # Change to the desired line number
line = read_line_number(file_path, line_number)
print(f"Line {line_number}: {line}")
