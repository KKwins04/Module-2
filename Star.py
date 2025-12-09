import turtle

turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()
#First triangle for star
board.forward(100) #draw base

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(120)
board.forward(100)

#Second triangle for star
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done()