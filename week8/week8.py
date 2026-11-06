# def getGrade(m):
#     if m >= 90:
#         return "A"
#     elif m >= 80:
#         return "B"
#     elif m >= 70:
#         return "C"
#     elif m >= 60:
#         return "D"
#     else:
#         return "F"
#
# mark = int(input("Enter mark: "))
# print(getGrade(mark))

def drawBar(t,h):
    if h<0:
        t.write(h)
        t.right(90)
        t.forward(-h)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(-h)
        t.right(90)
        t.backward(50)
        t.forward(50)
    else:
        t.left(90)
        t.forward(h)
        t.write(h)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(h)
        t.left(90)
        t.backward(50)
        t.forward(50)

def drawBarColor(t,h):
    if h>=200:
        t.fillcolor("red")
        t.begin_fill()
        drawBar(t,h)
        t.end_fill()
    elif h>=100:
        t.fillcolor("yellow")
        t.begin_fill()
        drawBar(t,h)
        t.end_fill()
    elif h>=0:
        t.fillcolor("green")
        t.begin_fill()
        drawBar(t,h)
        t.end_fill()
    else:
        t.fillcolor("hotpink")
        t.begin_fill()
        drawBar(t,h)
        t.end_fill()

import turtle

data = []
n = 0
while 1:
    n = input("Enter a number: ")
    if n=='':
        break
    data.append(int(n))

wn = turtle.Screen()
alex = turtle.Turtle()

for d in data:
    drawBarColor(alex,d)
wn.exitonclick()

# def findHypot(a,b):
#     return (a**2 + b**2)**0.5
#
# a = float(input("Write first side of the triangle: "))
# b = float(input("Write second side of the triangle: "))
# print(findHypot(a,b))