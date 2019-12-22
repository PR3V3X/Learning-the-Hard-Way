name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 * 2.54 # cm -> in
weight = round(180 * 453.59 * 0.001, 2) # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds tall.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teetch are usually {teeth} depending of the coffee.")

# this line is tricky, try to get it exactly right.
total = round(age + height + weight, 2)
print(f"If I add {age}, {height}, and {weight} I get {total}.")

