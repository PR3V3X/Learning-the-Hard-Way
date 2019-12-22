# Defines a string for 4 sets of {}.
formatter = "{} {} {} {}"

# Uses the .format function to replace the 4 variables in the {}, and prints.
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "theee", "four"))
print(formatter.format(True, False, False, True))

# Similar to above, puts the 4 sets of {} in the formatter string.
print(formatter.format(formatter, formatter, formatter, formatter))

# This is the same, just changed to be more "pythonic".
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
