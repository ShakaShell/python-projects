# Michael Roberts
# Section 11
# On my honor, I have neither received nor given any unauthorized assistance on this assignment.

import turtle

turtleName = turtle.Turtle()
screenName = turtle.Screen()

screenName.bgcolor("pink")
screenName.title("My Shape is Cool")
screenName.screensize(400,300)

turtleName.color("black")
turtleName.speed(5)

# used in drawNeck
def drawSquare(side):
    for i in range(4):
        turtleName.forward(side)
        turtleName.right(90)
        
# used in drawTopHair
def drawRect(length,width):
    for i in range(2):
        turtleName.forward(length)
        turtleName.left(90)
        turtleName.forward(width)
        turtleName.left(90)

# I did not make a drawCircle or drawArc function, as it would not make sense too 
# as it is already a function of turtle. I use square, rectangle, circle, and arc
# in my drawing (3/3 shapes).

# uses circle(dot) function of turtle
def drawHead(x, y):
    turtleName.penup()
    turtleName.goto(x, y)
    turtleName.pendown()
    turtleName.dot(600, "tan")

# uses drawSquare
def drawNeck(x, y):
    turtleName.penup()
    turtleName.goto(x, y)
    turtleName.color("tan")
    turtleName.pendown()
    turtleName.fillcolor("tan")
    turtleName.begin_fill()
    drawSquare(200)
    turtleName.end_fill()


# uses circle(dot) function of turtle
def drawEyeball(x, y):
    turtleName.penup()
    turtleName.goto(x, y)
    turtleName.pendown()
    turtleName.dot(150, "white")


# uses circle(dot) function of turtle
def drawPupil(x, y):
    turtleName.penup()
    turtleName.goto(x, y)
    turtleName.pendown()
    turtleName.dot(60, "black")

# uses the circle(arc) function of turtle
def drawMouth(x, y):
    turtleName.penup()
    turtleName.goto(x, y)
    turtleName.pendown()
    turtleName.right(96)
    turtleName.circle(90, 170)


# my own function to make what looks like a nose
def drawNose(x, y):
    turtleName.penup()
    turtleName.goto(x, y)
    turtleName.pendown()
    turtleName.right(180)
    turtleName.forward(90)
    turtleName.left(90)
    turtleName.forward(45)

# uses drawRectangle function
def drawTopHair(x, y):
    turtleName.penup()
    turtleName.goto(x, y)
    turtleName.pendown()
    turtleName.fillcolor("blue")
    turtleName.begin_fill()
    turtleName.left(20)
    drawRect(500,75)
    turtleName.end_fill()

# uses circle(arc) function of turtle
def drawSideHair(x, y):
    turtleName.penup()
    turtleName.goto(x, y)
    turtleName.pendown()
    turtleName.left(180)
    turtleName.fillcolor("blue")
    turtleName.begin_fill()
    turtleName.circle(80, 180)
    turtleName.end_fill()


# drawing begins

drawHead(0, 0)
turtle.setheading(0)
drawNeck(-100,-275)
drawEyeball(-110,90) # left eyeball
drawEyeball(110, 90) # right eyeball
drawPupil(-110,90) # left pupil
drawPupil(110, 90) # right pupil
turtleName.pensize(20)
turtleName.color("red")
drawMouth(-110, -90) 
turtleName.pensize(5)
turtleName.color("black")
drawNose(0, 20)
turtleName.pensize(0)
turtleName.color("blue")
drawTopHair(-225, 215)
drawSideHair(-225, 215)

turtleName.hideturtle()
turtle.done()





