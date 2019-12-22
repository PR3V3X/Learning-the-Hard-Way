# Imports the argv function from the sys module.
from sys import argv

# Takes 2 args (the .py file & the .txt file).
script, input_file = argv

# When called, will read the contents of .txt file.
def print_all(f):
    print(f.read())

# When called, will set seek position to 0.
def rewind(f):
    f.seek(0)

# When called, will print line # & contents of line.
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")


# Sets variable to open the file.
current_file = open(input_file)

print("First let's print the whole file:\n")

# Calls print_all func to prints contents of file.
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Calls rewind func to set to seek position to 0.
rewind(current_file)

print("Let's print three lines:")

# current_line is set to 1, after which gets +1'ed each line to 3.
# print_a_line func gets called, then current_line sets the seek position.
# current_file open the input_file (the .txt file).
# How does the seek position get changed though?
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
