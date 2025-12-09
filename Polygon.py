import turtle #importing library
turtle.Screen().bgcolor("red")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle() #define variable

num_sides = 6 #variable
side_length = 70
angle = 360.0 / num_sides
#iterate loop for total number of sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()