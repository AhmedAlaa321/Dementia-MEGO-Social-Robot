import turtle
from time import sleep

def initialize():
    turtle.setup(800,484)
    turtle.bgcolor("cyan")
    turtle.Turtle().hideturtle()

def drawEyes(angle):
    turtle.hideturtle()
    turtle.color("black","black")
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(120,0)
    turtle.pendown()
    turtle.circle(angle)
    turtle.penup()
    turtle.goto(-120,0)
    turtle.pendown()
    turtle.circle(angle)
    turtle.penup()
    turtle.end_fill()
    turtle.hideturtle()
    
def drawMouth(angle):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-80,-80)
    turtle.right(90)
    turtle.pendown()
    turtle.circle(angle,180)
    turtle.penup()
    turtle.hideturtle()

def startEmotion():
    turtle.reset()
    turtle.speed(0)

def endEmotion():
    turtle.hideturtle()
    turtle.done()
    
def normalEmotion():
    while 1:
        for degree in range(1,40,1):
            startEmotion()
            drawEyes(degree)
            drawMouth(degree*2)
        for degree in range(40,1,-1):
            startEmotion()
            drawEyes(degree)
            drawMouth(degree*2)
    endEmotion()

    
