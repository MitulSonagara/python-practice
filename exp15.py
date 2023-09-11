with open("input_file.txt", "r") as input_file, open("output_file.txt", "w") as output_file:
    lines = input_file.readlines()
    for i, line in enumerate(lines):
        if i != 4:  # Skip line 5 (index 4)
            output_file.write(line)
