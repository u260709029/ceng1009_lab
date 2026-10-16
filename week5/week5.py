# import random
# for i in range(10):
#     print(random.random())
# import math
# import random
# for i in range(10):
#     print(random.randint(25,35))

# import math
# first_side = int(input("Enter the length of first side:"))
# second_side = int(input("Enter the length of second side:"))
# print("The length of the hypotenuse is:",math.hypot(first_side,second_side))

# import math
# def areaOfCircle(r):
#     return math.pi * (r**2)
#
# radius = float(input("Enter the radius of the circle: "))
# print("The circumference of the circle is:", areaOfCircle(radius))

# import turtle
# def drawStar(t,side):
#     t.right(108)
#     for i in range(5):
#         t.forward(100)
#         t.left(144)
#
# wn = turtle.Screen()
# star = turtle.Turtle()
# drawStar(star,100)
#
# wn.exitonclick()

# import turtle
# def drawSquare(t,s):
#     for i in range(4):
#         t.forward(s)
#         t.left(90)
#
# wn = turtle.Screen()
# square = turtle.Turtle()
# side = int(input("Enter the side of the square: "))
# times = int(input("Enter the number of number of squares you want to draw: "))
# for i in range(times):
#     drawSquare(square,side)
#     square.penup()
#     square.forward(side*2)
#     square.pendown()
#
# wn.exitonclick()

import turtle
def drawSquareGetBigger(t,s,n,c):
    for i in range(n):
        for j in range(4):
            t.forward(s)
            t.left(90)
        s = s+increase
        t.penup()
        t.goto(t.xcor()-(increase/2),t.ycor()-(increase/2))
        t.pendown()

wn = turtle.Screen()
square = turtle.Turtle()
side = int(input("Enter the side of the square:"))
times = int(input("Enter the number of number of squares you want to draw:"))
increase = int(input("Enter the increase amount of the side of the square:"))
drawSquareGetBigger(square,side,times,increase)

wn.exitonclick()