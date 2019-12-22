# Defines a function that takes 2 args.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # f-strings printing value in args.
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")

    # Stings giving more information.
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

def juice(boxes_of_juice, number_of_juices):
    print(f"There are {boxes_of_juice} boxes of juice.")
    print(f"Each box contains {number_of_juices} juices.")
    print("That's alot of juice!!! \n")


# You can pass #'s into the function.
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


# You can set a variable that will pass #'s into the function.
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# Calls the function with the variables.
# amt_of_che = che_cou = 10
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Math can be done inside, and passed to function.
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Setting a variable amt, and math can be done to the function too.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


juice(10, 8)

boxes = 30
amount = 10

juice(boxes, amount)

juice(15 + 25, 9 + 10)

juice(boxes + 10, amount * 4)
