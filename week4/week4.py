# for i in range(100):
#     print("We like Python's turtles!")

# for i in["January","February","March","April","May","June","July","August","September","October","November","December"]:
#     print("One of the months of the year is",i)

# for i in[12, 10, 32, 3, 66, 17, 42, 99, 20]:
#     print(i, i**2)

# import turtle
# wn = turtle.Screen()
# ilter = turtle.Turtle()
# ilter.color("red")
# for i in range(3):
#     ilter.forward(100)
#     ilter.left(120)
#
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# ilter = turtle.Turtle()
# ilter.color("blue")
# for i in range(4):
#     ilter.forward(100)
#     ilter.left(90)
#
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# ilter = turtle.Turtle()
# ilter.color("pink")
# for i in range(6):
#     ilter.forward(100)
#     ilter.left(60)
#
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# ilter = turtle.Turtle()
# ilter.color("green")
# for i in range(8):
#     ilter.forward(100)
#     ilter.left(45)
#
# wn.exitonclick()

# import turtle
# sides = int(input("Enter the number of sides:"))
# length = int(input("Enter the length of the sides:"))
# colour = input("Enter the colour of the sides:")
# fill_colour = input("Enter the fill colour of the polygon:")
# wn = turtle.Screen()
# ilter = turtle.Turtle()
# ilter.color(colour)
# ilter.fillcolor(fill_colour)
# ilter.begin_fill()
# for i in range(sides):
#     ilter.forward(length)
#     ilter.left(360/sides)
# ilter.end_fill()
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# pirate = turtle.Turtle()
# pirate.color("yellow")
# for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
#     pirate.forward(100)
#     pirate.left(i)
# print(pirate.heading())
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# ilter = turtle.Turtle()
# ilter.color("orange")
# ilter.right(108)
# for i in range(5):
#     ilter.forward(100)
#     ilter.left(144)
#
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# ilter = turtle.Turtle()
# ilter.color("grey")
# ilter.shape("turtle")
# ilter.penup()
# ilter.forward(100)
# for i in range(12):
#     ilter.pendown()
#     ilter.forward(10)
#     ilter.penup()
#     ilter.forward(15)
#     ilter.stamp()
#     ilter.left(180)
#     ilter.forward(125)
#     ilter.right(150)
#     ilter.forward(100)
# ilter.goto(0,0)
# wn.exitonclick()

import turtle
legs = int(input("Please enter the number of legs:"))
wn = turtle.Screen()
spider = turtle.Turtle()
spider.shape("turtle")
spider.right(90)
spider.stamp()
spider.left(90)
spider.penup()
for i in range(legs):
    spider.pendown()
    spider.forward(100)
    spider.penup()
    spider.left(180)
    spider.forward(100)
    spider.right(180-360/legs)
spider.right(90)
wn.exitonclick()