# --setup--

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

# --functions--

def drawPoly(someturtle,someside,somesize):
    for i in range(someside):
        someturtle.forward(somesize)
        someturtle.left(360/someside)

def drawSpiral(someturtle,someside,someangle):
    for i in range(someside):
        someturtle.backward((i + 2) * 2)
        someturtle.right(someangle)

def upGoTo(someturtle,somex,somey):
    someturtle.penup()
    someturtle.goto(somex, somey)
    someturtle.pendown()

def drawEquiTriangle(someturtle,somesize):
    drawPoly(someturtle,3,somesize)

def drawStar(someturtle,somesize):
    for i in range(5):
        someturtle.forward(somesize)
        someturtle.right(144)

def drawSprite(someturtle,somelegs,somelength):
    x=someturtle.xcor()
    y=someturtle.ycor()
    for i in range(somelegs):
        someturtle.forward(somelength)
        upGoTo(someturtle,x,y)
        someturtle.left(360/somelegs)

# --exercises--

# Exercise_1

# tess.pensize(2)
# tess.color("hotpink")
# drawPoly(tess,8,50)

# Exercise_2

# tess.color("blue")
# tess.pensize(2)
# for i in range(20):
#     drawPoly(tess,4,100)
#     tess.left(18)

# Exercise_3

# tess.speed(50)
# tess.color("blue")
# tess.pensize(2)
# upGoTo(tess,-150,0)
# drawSpiral(tess,100,90)
# upGoTo(tess,150,0)
# drawSpiral(tess,100,89)

# Exercise_4

# drawEquiTriangle(tess,50)

# Exercise_5

# tess.color("hotpink")
# tess.pensize(2)
# upGoTo(tess,-150,0)
# for i in range(5):
#     drawStar(tess,100)
#     tess.penup()
#     tess.forward(350)
#     tess.right(144)
#     tess.pendown()

# Exercise_6

tess.shape("turtle")
tess.right(90)
tess.stamp()
tess.left(90)
drawSprite(tess,15,120)
tess.right(90)

# --finish--

wn.exitonclick()