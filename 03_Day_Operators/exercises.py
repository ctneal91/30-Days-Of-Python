
# 1. Declare your age as integer variable
age = 33

# 2. Declare your height as a float variable
height = 73.0

# 3. Declare a variable that store a complex number
variable = 2 + 2j
# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
print("Problem 4: Calculate the area of a triangle")
print("Enter base:")
base = input()
print("Enter height:")
height = input()
print("The area of the triangle is", int(base) * int(height) * 0.5)
print("\n")

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
print("Problem 5: Calculate the perimeter of a triangle")
print("Enter side a length:")
a = int(input())
print("Enter side b length:")
b = int(input())
print("Enter side c length:")
c = int(input())
print("The perimeter of the triangle is", a + b + c)
print("\n")

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
print("Problem 6: Calculate the area and perimeter of a rectangle")
print("Enter rectangle length:")
rectangle_length = int(input())
print("Enter rectangle height:")
rectangle_width = int(input())
area_of_rectangle = rectangle_length * rectangle_width
perimeter_of_rectangle = 2 * (rectangle_length + rectangle_width)
print("Rectangle area is", area_of_rectangle, "units squared")
print("Rectangle perimeter is", area_of_rectangle, "units")
print("\n")

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
print("Problem 7: Calculate the area and circumference of a circle")
pi = 3.14
print("Enter radius:")
radius = int(input())
print("Area of the circle is", pi * radius ** 2)
print("Perimeter of the circle is", 2 * radius * pi)
print("\n")

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
print("Problem 8: Calculate the slope, x-intercept and y-intercept of y = 2x - 2")
def this_equation(x):
    return 2*x - 2

y_intercept = this_equation(0)
print(y_intercept)

x_intercept =(0 + 2) / 2
print(x_intercept)

def this_equation_slope():
    y2 = this_equation(1)
    y1 = this_equation(0)
    return (y2 - y1)
problem_8_slope = this_equation_slope()
print(problem_8_slope)
print("\n")

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) between point (2, 2) and point (6,10)
print("Problem 9: Calculate the slope and Euclidean distance between point (2, 2) and point (6,10)")
def calculate_slope(point_one, point_two):
   return (point_two[1] - point_one[1]) / (point_two[0] - point_one[0])
   
def euclidean_distance(point_one, point_two):
    return ((point_two[0] - point_one[0]) ** 2 + (point_two[1] - point_one[1]) ** 2) ** 0.5

point_one = [2, 2]
point_two = [6, 10]

problem_9_slope = calculate_slope(point_one, point_two)
print("The slope is:", problem_9_slope)
print("The Euclidean distance is:", euclidean_distance(point_one, point_two))
print("\n")

# 10. Compare the slopes in tasks 8 and 9.
print("Problem 10: Compare the slopes in tasks 8 and 9")
slope_difference = problem_8_slope - problem_9_slope
print(slope_difference)
print("\n")

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
print("Problem 11: Calculate the value of y (y = x^2 + 6x + 9) for different x values")
def parabolic_equation(x):
    return(x ** 2 + 6 * x + 9)

print("here is a bunch of points for the equation y = x^2 + 6x + 9")
print("(-3, ", parabolic_equation(-3), ")", sep="")
print("(-2, ", parabolic_equation(-2), ")", sep="")
print("(-1, ", parabolic_equation(-1), ")", sep="")
print("(0, ", parabolic_equation(0), ")", sep="")
print("(1, ", parabolic_equation(1), ")", sep="")
print("(2, ", parabolic_equation(2), ")", sep="")
print("(3, ", parabolic_equation(3), ")", sep="")
print("\n")

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement
print("Problem 12: Find the length of 'python' and 'dragon' and make a falsy comparison statement")
print("Python and dragon aren't the same length:", len('python') is not len('dragon'))
print("\n")

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("Problem 14: I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.")
print("Is 'jargon' in the sentence, 'I hope this course is not full of jargon.'?", "jargon" in "I hope this course is not full of jargon.")
print("\n")

# 15. There is no 'on' in both dragon and python
print("Problem 15: There is no 'on' in both dragon and python")
print("There is no 'on' in both dragon and python: ", "on" not in 'dragon' and "on" not in "python")
print("\n")

# 16. Find the length of the text python and convert the value to float and convert it to string
print("Problem 16: Find the length of the text python and convert the value to float and convert it to string")
print(str(float(len("python"))))
print("\n")

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print("Problem 17: Check if a number is even or not using python")
def is_even(x):
    return x % 2 is 0

print("2 is even:", is_even(2))
print("3 is even:", is_even(3))
print("\n")


# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print("Problem 18: Check if the floor division of 7 by 3 is equal to the int converted value of 2.7")
print("Floor division of 7 by 3 is equal to the integer value of 2.7:", 7 // 3 is int(2.7))
print("\n")

# 19. Check if type of '10' is equal to type of 10
print("Problem 19: Check if type of '10' is equal to type of 10")
print("Type of '10' is the same type as 10: ", type('10') is type(10))
print("\n")

# 20. Check if int('9.8') is equal to 10
print("Problem 20: Check if int('9.8') is equal to 10")
print("Is int('9.8') equal to 10?", int(float('9.8')) is 10)
print("\n")

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
print("Problem 21: Calculate pay of the person")
print("Enter your pay rate per hour:")
rate = int(input())
print("Enter your hours:")
hours = int(input())
print("Your pay should be $", rate * hours, sep="")
print("\n")

