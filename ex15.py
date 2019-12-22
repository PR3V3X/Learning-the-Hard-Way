# Import the argv function from the sys module.
from sys import argv

# Asks for 2 variables (name of .py file & .txt file).
script, filename = argv

# Assigns txt variable to open the .txt file.
txt = open(filename)

# Prints an f-string showing .txt filename.
print(f"Here's your file {filename}:")

# Prints the contents of the .txt file.
print(txt.read())

# Closes the .txt file.
txt.close()

# Prints a string asking for the .txt filename.
print("Type the filename again:")

# Takes input for the .txt filename.
file_again = input('> ')

# Assigns txt_again variable to open the .txt file.
txt_again = open(file_again)

# Prints the contents of the .txt file.
print(txt_again.read())

# Closes the .txt file.
txt_again.close()


