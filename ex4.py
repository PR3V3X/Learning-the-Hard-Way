# Number of cars.
cars = 100

# Number of drivers.
drivers = 30

# Difference of cars and drivers.
cars_not_driven = cars - drivers

# Cars driven is equal to drivers.
cars_driven = drivers

# MOST cars have 4 seats.
space_in_a_car = 4

# Number of seats being used by cars driven.
carpool_capacity = cars_driven * space_in_a_car

# Number of people being driven.
passengers = 90

# Average amount of people being driven.
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
    "in each car.")

