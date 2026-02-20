# Day 2: 30 Days of python programming
# Level 1
# Declare a first name variable and assign a value to it
first_name = 'Michael'

# Declare a last name variable and assign a value to it
last_name = 'Phelps'

# Declare a full name variable and assign a value to it
full_name = first_name + last_name

# Declare a country variable and assign a value to it
country = 'USA'

# Declare a city variable and assign a value to it
city = 'Baltimore'

# Declare an age variable and assign a value to it
age = 40

# Declare a year variable and assign a value to it
year = 2026

# Declare a variable is_married and assign a value to it
is_married = True
# Declare a variable is_true and assign a value to it
is_true = True

# Declare a variable is_light_on and assign a value to it
is_light_on = False

# Declare multiple variable on one line
medal_count, olympics = 23 + 3 + 2, [2000, 2004, 2008, 2012, 2016]

# Level 2
# 1. Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(medal_count))
print(type(olympics))

# Using the len() built-in function, find the length of your first name
print(len(first_name))

# Compare the length of your first name and your last name
print(len(first_name) - len(last_name))
# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = sum([num_one, num_two])

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(remainder)

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# The radius of a circle is 30 meters.
radius = 30

# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = radius ** 2 * 3.14

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = radius * 2 * 3.14
# Take radius as user input and calculate the area.
print("Enter radius of circle:")
user_radius = input()
print("Area of the circle", int(user_radius) ** 2 * 3.14)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
print("Enter first name, last_name, country and age:")
user_first_name, user_last_name, user_country, user_age = input(), input(), input(), input()

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')