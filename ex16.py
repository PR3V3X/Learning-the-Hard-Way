# Imports the argv function from the sys module.
from sys import argv

# Takes 2 arguments (.py filename & .txt filename).
script, filename = argv

# Lets the user know what is going on.
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN (ENTER).")

# Asks for an input from the user.
input("?")

# Opens the file file in write (truncates, then writes) mode.
print("Opening the file...")
target = open(filename, 'w')

# Truncates contents of the file. This bit code isn't needed.
print("Truncating the file. Goodbye!")
target.truncate()

# Takes 3 user inputs for new lines.
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Writes the lines from the inputs and a new line after it.
print("I'm going to write these to the file.")

target.write(f"{line1} \n{line2} \n{line3}\n")


# Closes the file.
print("And finally, we close it.")
target.close()


# Example code for study drills.
'''
from sys import argv

script, filename = argv

print(f"This is going to read the file: {filename}.")

txt = open(filename)
print(txt.read())
txt.close()
'''
