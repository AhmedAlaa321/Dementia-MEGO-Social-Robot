from turtle import Turtle, Screen, Shape
from time import sleep
import turtle
screen = turtle.Screen()
cursor = turtle.Turtle()

def initialize():
    turtle.setup(800, 484)
    turtle.bgcolor("cyan")
    cursor.hideturtle()

def __startEmotion():
    turtle.reset()
    turtle.speed(0)

def __endEmotion():
    cursor.hideturtle()
    turtle.done()

def __startFunction():
    turtle.hideturtle()
    turtle.speed(0)

def __drawEndFunction():
    turtle.reset()

def __drawEyes():
    __startFunction()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.color("black", "black")
    eyes = Shape("compound")
    turtle.begin_poly()
    turtle.goto(-80,0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.end_poly()
    lefteye = turtle.get_poly()
    eyes.addcomponent(lefteye, "black", "cyan")
    turtle.begin_poly()
    turtle.pendown()
    turtle.goto(80,0)
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.end_poly()
    righteye = turtle.get_poly()
    eyes.addcomponent(righteye, "black", "cyan")
    screen.addshape("Eyes", eyes)
    __drawEndFunction()

def __showEyes():
    __startFunction()
    __drawEyes()
    eyes = turtle.Turtle("Eyes")
    eyes.speed(0)
    eyes.penup()
    eyes.left(90)
    eyes.goto(-5, 20)
    eyes.resizemode("user")
    eyes.shapesize(1.5, 3)

def __drawMouth():
    __startFunction()
    turtle.color("black", "black")
    turtle.begin_poly()
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(200, 60)
    turtle.end_fill()
    turtle.end_poly()
    lowerlips = turtle.get_poly()
    screen.addshape("LowerLips", lowerlips)
    turtle.color("cyan", "cyan")
    turtle.begin_poly()
    turtle.begin_fill()
    turtle.circle(160, 60)
    turtle.end_fill()
    turtle.end_poly()
    upperlips = turtle.get_poly()
    screen.addshape("UpperLips", upperlips)
    __drawEndFunction()

def __showMouth():
    __startFunction()
    __drawMouth()
    lowerlips = turtle.Turtle("LowerLips")
    lowerlips.speed(0)
    lowerlips.penup()
    lowerlips.goto(-100, -130)
    lowerlips.left(60)
    upperlips = turtle.Turtle("UpperLips")
    upperlips.color("cyan")
    upperlips.speed(0)
    upperlips.penup()
    upperlips.goto(-179, 45)

def __drawNose():
    __startFunction()
    turtle.color("black", "black")
    turtle.begin_poly()
    turtle.begin_fill()
    turtle.left(90)
    turtle.fd(30)
    turtle.left(90)
    turtle.fd(10)
    turtle.left(90)
    turtle.fd(30)
    turtle.left(90)
    turtle.fd(10)
    turtle.end_fill()
    turtle.end_poly()
    nose = turtle.get_poly()
    screen.addshape("Nose", nose)
    __drawEndFunction()

def __showNose():
    __startFunction()
    __drawNose()
    nosedraw = turtle.Turtle("Nose")
    nosedraw.speed(0)
    nosedraw.left(90)
    nosedraw.bk(10)

def __blinkEyes():
    __startFunction()
    __drawEyes()
    eyes = turtle.Turtle("Eyes")
    eyes.speed(0)
    eyes.penup()
    eyes.left(90)
    eyes.goto(-5, 20)
    eyes.resizemode("user")
    eyes.shapesize(1.5, 3)
    while 1:
        sleep(4)
        eyes.hideturtle()
        sleep(0.1)
        eyes.showturtle()

def __talk():
    __startFunction()
    __drawMouth()
    lowerlips = turtle.Turtle("LowerLips")
    lowerlips.speed(0)
    lowerlips.penup()
    lowerlips.goto(-100, -130)
    lowerlips.left(60)
    upperlips = turtle.Turtle("UpperLips")
    upperlips.color("cyan")
    upperlips.speed(0)
    upperlips.penup()
    upperlips.goto(-179, 45)
    while 1:
        sleep(0.1)
        upperlips.hideturtle()
        sleep(0.1)
        upperlips.showturtle()

def normalEmotion():
    __startEmotion()
    __showMouth()
    __showNose()
    __blinkEyes()
    __endEmotion()

def talkingEmotion():
    __startEmotion()
    __showEyes()
    __showNose()
    __talk()
    __endEmotion()


