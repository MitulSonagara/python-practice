def is_file_empty(file_path):
    with open(file_path, 'r') as file:
        return not bool(file.read())

file_path = "input_file.txt"  # Replace with the path to your file
if is_file_empty(file_path):
    print("The file is empty.")
else:
    print("The file is not empty.")
