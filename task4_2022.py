'''
Open the file SQUARE_SIDE.py
You will see the following function that:
•	Takes the perimeter of a square as a parameter
•	Returns the length of each side of the square
'''
def square_side(sq_perimeter):
   side_length = sq_perimeter / 4
   return side_length
'''
#####################################
Question 10 [4]
Extend the program by writing another function square_area() that:
a.	Takes the perimeter as a parameter
b.	Calculates the area of the square
c.	Returns the area of the square
Your function must use square_side().
The calculation for the area of a square is:
  Area = length of side x length of side

Save your program as SQUARE_2022_<your name>_<centre number>_<index number>.py
'''
########################################
def square_area(sq_perimeter):
    length = square_side(sq_perimeter)
    area = length*length
    return area
var1 = square_area(40)
print(var1)

  

'''
Question 11 [3]

In your program, write the function circle_diam(), to calculate and 
return the diameter of a circle. The parameter circumference must be passed to the function.

The calculation required for the diameter of a circle is :
  Diameter = circumference / 3.14

Save your program as CIRCLE_2022_<your name>_<centre number>_<index number>.py
'''
##############################################
def circle_diam(circumference):
    diameter = circumference / 3.14
    return diameter
circle1 = circle_diam(50)
print(circle1)

'''
Question 12 [3]
Extend your program by writing another function circle_area() that:
a.	Takes the circumference as a parameter
b.	Calculates the area of the circle
c.	Returns the area of the circle

Your function must use circle_diam()
The calculation required for the area of a circle is:
  Area = 3.14 x radius x radius

The radius of a circle is half the diameter.

Save your program.
'''
###############################################
def circle_area(circumference):
    radius = circle_diam(circumference)/2
    area = 3.14 * radius * radius
    return area
circle2 = circle_area(20)
print(circle2)
'''
Question 13 [10]

Save your program as SHAPES_2022_<your name>_<centre number>_<index number>.py

Extend your program to create a user interface. The program must:
a.	Allow the user to input whether they want to find the area of a square or a circle, 
with a suitable input message

b.	Loop until the user enters a valid shape (square or circle), 
with a suitable error message

c.	Allow the user to input the perimeter of the square, 
if they want to find the area of a square

d.	Allow the user to input the circumference of the circle, 
if they want to find the area of a circle.

e.	Calculate the area for the shape input by the yser, 
using the correct functions

f.	display the area of the shape input by the user.

To display the area of the shape input by the user, 
write another function output_message() that takes the appropriate parameters 
to return the message:

“The area of the X is Y”

X should be replaced with the name of the shape and Y should be replace 
with the value for the area of the shape. For example:

“The area of the square is 50.41”

Save your program 

'''
def output_message(shape,area):
    message = "The area of the " + shape + " is " + str(area)
    return message



while True:
    question1 = input("Do you want to find the area of a circle or a square? ")
    question1 = question1.lower()
    if question1 == "square" or question1 == "circle":
        break
    else:
        print("Invalid input, you need to enter a circle or a square. ")
if question1 == "square":
    perimetersquare = int(input("What is the perimeter of the square? "))
    squarearea = square_area(perimetersquare)
    print(output_message(question1,squarearea))
else:
    circumference_circle = int(input("what is the circumference of your circle? "))
    circlearea = circle_area(circumference_circle)
    print(output_message(question1,circlearea))



