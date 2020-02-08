from turtle import Turtle, Screen, Shape
from time import sleep
import turtle
import multiprocessing
screen = turtle.Screen()
cursor = turtle.Turtle()

def initialize():
    turtle.setup(800, 484)
    turtle.bgcolor("cyan")
    cursor.hideturtle()

def __startEmotion():
    turtle.reset()
    turtle.speed(0)
    screen.tracer(0)

def __endEmotion():
    cursor.hideturtle()
    turtle.done()

def __startFunction():
    turtle.hideturtle()
    turtle.speed(0)
    screen.tracer(0)
    turtle.penup()
    turtle.goto(0, 0)

def __drawEndFunction():
    turtle.reset()

def __drawEyes():
    __startFunction()

    #draw the eye when opened with mid cornea
    openeyes1 = Shape("compound")
    turtle.begin_poly()
    turtle.goto(-80, 0)
    turtle.pendown()
    turtle.circle(15)
    turtle.penup()
    turtle.end_poly()
    lefteye1 = turtle.get_poly()
    openeyes1.addcomponent(lefteye1, "black", "cyan")
    turtle.begin_poly()
    turtle.goto(80, 0)
    turtle.pendown()
    turtle.circle(15)
    turtle.penup()
    turtle.end_poly()
    righteye1 = turtle.get_poly()
    openeyes1.addcomponent(righteye1, "black", "cyan")

    #place the cornea mid the openedeyes
    turtle.begin_poly()
    turtle.penup()
    turtle.goto(-80, 0)
    turtle.pendown()
    turtle.circle(8)
    turtle.penup()
    turtle.end_poly()
    leftcornea1 = turtle.get_poly()
    openeyes1.addcomponent(leftcornea1, "cyan", "cyan")
    turtle.begin_poly()
    turtle.penup()
    turtle.goto(80, 0)
    turtle.pendown()
    turtle.circle(8)
    turtle.penup()
    turtle.end_poly()
    rightcornea1 = turtle.get_poly()
    openeyes1.addcomponent(rightcornea1, "cyan", "cyan")
    screen.addshape("OpenedEyesM", openeyes1)

    # draw the eye when opened with left cornea
    openeyes2 = Shape("compound")
    turtle.begin_poly()
    turtle.goto(-80, 0)
    turtle.pendown()
    turtle.circle(15)
    turtle.penup()
    turtle.end_poly()
    lefteye2 = turtle.get_poly()
    openeyes2.addcomponent(lefteye2, "black", "cyan")
    turtle.begin_poly()
    turtle.goto(80, 0)
    turtle.pendown()
    turtle.circle(15)
    turtle.penup()
    turtle.end_poly()
    righteye2 = turtle.get_poly()
    openeyes2.addcomponent(righteye2, "black", "cyan")

    # place the cornea left the openedeyes
    turtle.begin_poly()
    turtle.penup()
    turtle.goto(-83, 0)
    turtle.pendown()
    turtle.circle(8)
    turtle.penup()
    turtle.end_poly()
    leftcornea2 = turtle.get_poly()
    openeyes2.addcomponent(leftcornea2, "cyan", "cyan")
    turtle.begin_poly()
    turtle.penup()
    turtle.goto(77, 0)
    turtle.pendown()
    turtle.circle(8)
    turtle.penup()
    turtle.end_poly()
    rightcornea2 = turtle.get_poly()
    openeyes2.addcomponent(rightcornea2, "cyan", "cyan")
    screen.addshape("OpenedEyesL", openeyes2)

    # draw the eye when opened with Right cornea
    openeyes3 = Shape("compound")
    turtle.begin_poly()
    turtle.goto(-80, 0)
    turtle.pendown()
    turtle.circle(15)
    turtle.penup()
    turtle.end_poly()
    lefteye3 = turtle.get_poly()
    openeyes3.addcomponent(lefteye3, "black", "cyan")
    turtle.begin_poly()
    turtle.goto(80, 0)
    turtle.pendown()
    turtle.circle(15)
    turtle.penup()
    turtle.end_poly()
    righteye3 = turtle.get_poly()
    openeyes3.addcomponent(righteye3, "black", "cyan")

    # place the cornea Right the openedeyes
    turtle.begin_poly()
    turtle.penup()
    turtle.goto(-77, 0)
    turtle.pendown()
    turtle.circle(8)
    turtle.penup()
    turtle.end_poly()
    leftcornea3 = turtle.get_poly()
    openeyes3.addcomponent(leftcornea3, "cyan", "cyan")
    turtle.begin_poly()
    turtle.penup()
    turtle.goto(83, 0)
    turtle.pendown()
    turtle.circle(8)
    turtle.penup()
    turtle.end_poly()
    rightcornea3 = turtle.get_poly()
    openeyes3.addcomponent(rightcornea3, "cyan", "cyan")
    screen.addshape("OpenedEyesR", openeyes3)

    #draw the eye when closed
    closeeyes = Shape("compound")
    turtle.begin_poly()
    turtle.goto(-80, 0)
    turtle.pendown()
    turtle.fd(28)
    turtle.left(90)
    turtle.fd(2)
    turtle.left(90)
    turtle.fd(28)
    turtle.left(90)
    turtle.fd(2)
    turtle.end_poly()
    leftcloseeye = turtle.get_poly()
    closeeyes.addcomponent(leftcloseeye, "black", "cyan")
    turtle.penup()
    turtle.begin_poly()
    turtle.goto(80, 0)
    turtle.pendown()
    turtle.left(90)
    turtle.fd(28)
    turtle.left(90)
    turtle.fd(2)
    turtle.left(90)
    turtle.fd(28)
    turtle.left(90)
    turtle.fd(2)
    turtle.end_poly()
    rightcloseeye = turtle.get_poly()
    closeeyes.addcomponent(rightcloseeye, "black", "cyan")
    screen.addshape("ClosedEyes", closeeyes)

    __drawEndFunction()

def __showEyes():
    __startFunction()
    __drawEyes()
    screen.update()
    eyes = turtle.Turtle("OpenedEyesM")
    eyes.speed(0)
    eyes.penup()
    eyes.left(90)
    eyes.goto(-5, 20)
    eyes.resizemode("user")
    eyes.shapesize(2, 3)

def __drawMouth():
    __startFunction()

    #draw the lower lips of the mouth
    turtle.color("black", "black")
    turtle.begin_poly()
    turtle.begin_fill()
    turtle.pensize(10)
    turtle.circle(300, 60)
    turtle.end_fill()
    turtle.end_poly()
    lowerlips = turtle.get_poly()
    screen.addshape("LowerLips", lowerlips)

    #draw the upper lips of the mouth
    turtle.color("cyan", "cyan")
    turtle.pensize(10)
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
    screen.update()
    lowerlips = turtle.Turtle("LowerLips")
    lowerlips.speed(0)
    lowerlips.penup()
    lowerlips.goto(-145, -130)
    lowerlips.left(60)
    upperlips = turtle.Turtle("UpperLips")
    upperlips.color("cyan")
    upperlips.speed(0)
    upperlips.penup()
    upperlips.goto(-450, 130)
    upperlips.resizemode("user")
    upperlips.shapesize(1, 2)

def __drawNose():
    __startFunction()
    turtle.color("black", "black")
    turtle.begin_poly()
    turtle.penup()
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.end_poly()
    nose = turtle.get_poly()
    screen.addshape("Nose", nose)
    __drawEndFunction()

def __showNose():
    __startFunction()
    __drawNose()
    screen.update()
    nosedraw = turtle.Turtle("Nose")
    nosedraw.speed(0)
    nosedraw.penup()
    nosedraw.goto(-15, -10)
    nosedraw.resizemode("user")
    nosedraw.shapesize(3, 1)

def __drawEyeBrows():
    __startFunction()
    eyebrows = Shape("compound")

    #draw Left eye Brow
    turtle.begin_poly()
    turtle.penup()
    turtle.goto(-80, 0)
    turtle.left(5)
    turtle.pendown()
    turtle.fd(15)
    turtle.left(90)
    turtle.fd(5)
    turtle.left(90)
    turtle.fd(30)
    turtle.left(90)
    turtle.fd(5)
    turtle.left(90)
    turtle.fd(15)
    turtle.end_poly()
    leftbro = turtle.get_poly()
    eyebrows.addcomponent(leftbro, "black", "cyan")

    #draw Right Eye Borw
    turtle.penup()
    turtle.right(5)
    turtle.goto(80, 0)
    turtle.begin_poly()
    turtle.left(180)
    turtle.right(5)
    turtle.fd(15)
    turtle.right(90)
    turtle.fd(5)
    turtle.right(90)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(5)
    turtle.right(90)
    turtle.fd(15)
    turtle.end_poly()
    rightbro = turtle.get_poly()
    eyebrows.addcomponent(rightbro, "black", "cyan")
    screen.addshape("EyeBrows", eyebrows)
    __drawEndFunction()

def __showEyeBrows():
    __startFunction()
    __drawEyeBrows()
    browsdraw = turtle.Turtle("EyeBrows")
    browsdraw.speed(0)
    browsdraw.penup()
    browsdraw.left(90)
    browsdraw.goto(-5, 170)
    browsdraw.resizemode("user")
    browsdraw.shapesize(3, 4)

def __blinkEyes():
    __startFunction()
    __drawEyes()
    #show opened eyes with mid cornea
    openeyesm = turtle.Turtle("OpenedEyesM")
    openeyesm.speed(0)
    openeyesm.penup()
    openeyesm.left(90)
    openeyesm.goto(-5, 20)
    openeyesm.resizemode("user")
    openeyesm.shapesize(3, 4)

    #show opened eyes with left cornea
    openeyesl = turtle.Turtle("OpenedEyesL")
    openeyesl.speed(0)
    openeyesl.penup()
    openeyesl.left(90)
    openeyesl.goto(-5, 20)
    openeyesl.resizemode("user")
    openeyesl.shapesize(3, 4)

    #show opened eyes with right cornea
    openeyesr = turtle.Turtle("OpenedEyesR")
    openeyesr.speed(0)
    openeyesr.penup()
    openeyesr.left(90)
    openeyesr.goto(-5, 20)
    openeyesr.resizemode("user")
    openeyesr.shapesize(3, 4)

    #show closed eyes
    closeeyes = turtle.Turtle("ClosedEyes")
    closeeyes.speed(0)
    closeeyes.penup()
    closeeyes.left(90)
    closeeyes.goto(-33, 57)
    closeeyes.resizemode("user")
    closeeyes.shapesize(3, 4)

    while 1:

        #hide all the shapes first to avoid overlap
        openeyesr.hideturtle()
        openeyesl.hideturtle()
        openeyesm.hideturtle()
        screen.update()

        for count in range(0, 8, 1):
            if count == 4:
                # open eyes 4 sec with rightcornea then blink
                closeeyes.hideturtle()
                openeyesr.showturtle()
                screen.update()
                sleep(4)
                openeyesr.hideturtle()
                closeeyes.showturtle()
                screen.update()
                sleep(0.1)
            elif count == 5:
                # open eyes 4 sec with rightcornea then blink
                closeeyes.hideturtle()
                openeyesr.showturtle()
                screen.update()
                sleep(4)
                openeyesr.hideturtle()
                closeeyes.showturtle()
                screen.update()
                sleep(0.1)
            elif count == 6:
                # open eyes 4 sec with leftcornea then blink
                closeeyes.hideturtle()
                openeyesl.showturtle()
                screen.update()
                sleep(4)
                openeyesl.hideturtle()
                closeeyes.showturtle()
                screen.update()
                sleep(0.1)
            elif count == 7:
                # open eyes 4 sec with leftcornea then blink
                closeeyes.hideturtle()
                openeyesl.showturtle()
                screen.update()
                sleep(4)
                openeyesl.hideturtle()
                closeeyes.showturtle()
                screen.update()
                sleep(0.1)
            else:
                #open eyes 4 sec with mid cornea then blink
                closeeyes.hideturtle()
                openeyesm.showturtle()
                screen.update()
                sleep(4)
                openeyesm.hideturtle()
                closeeyes.showturtle()
                screen.update()
                sleep(0.1)

def __talkBlink():
    __startFunction()
    __drawMouth()
    __drawEyes()

    #draw lower lips
    lowerlips = turtle.Turtle("LowerLips")
    lowerlips.speed(0)
    lowerlips.penup()
    lowerlips.goto(-145, -130)
    lowerlips.left(60)

    #draw upper lips
    upperlips = turtle.Turtle("UpperLips")
    upperlips.color("cyan")
    upperlips.speed(0)
    upperlips.penup()
    upperlips.goto(-450, 130)
    upperlips.resizemode("user")
    upperlips.shapesize(1, 2)

    # show opened eyes with mid cornea
    openeyesm = turtle.Turtle("OpenedEyesM")
    openeyesm.speed(0)
    openeyesm.penup()
    openeyesm.left(90)
    openeyesm.goto(-5, 20)
    openeyesm.resizemode("user")
    openeyesm.shapesize(3, 4)

    # show opened eyes with left cornea
    openeyesl = turtle.Turtle("OpenedEyesL")
    openeyesl.speed(0)
    openeyesl.penup()
    openeyesl.left(90)
    openeyesl.goto(-5, 20)
    openeyesl.resizemode("user")
    openeyesl.shapesize(3, 4)

    # show opened eyes with right cornea
    openeyesr = turtle.Turtle("OpenedEyesR")
    openeyesr.speed(0)
    openeyesr.penup()
    openeyesr.left(90)
    openeyesr.goto(-5, 20)
    openeyesr.resizemode("user")
    openeyesr.shapesize(3, 4)

    # show closed eyes
    closeeyes = turtle.Turtle("ClosedEyes")
    closeeyes.speed(0)
    closeeyes.penup()
    closeeyes.left(90)
    closeeyes.goto(-33, 57)
    closeeyes.resizemode("user")
    closeeyes.shapesize(3, 4)

    while 1:

        # hide all the shapes first to avoid overlap
        openeyesr.hideturtle()
        openeyesl.hideturtle()
        openeyesm.hideturtle()
        upperlips.hideturtle()
        lowerlips.hideturtle()
        screen.update()

        for count in range(0, 8, 1):
            if count == 4:
                # open eyes 4 sec with rightcornea then blink
                closeeyes.hideturtle()
                openeyesr.showturtle()
                screen.update()
                for i in range(0, 20, 1):
                    upperlips.showturtle()
                    lowerlips.showturtle()
                    screen.update()
                    sleep(0.1)
                    upperlips.hideturtle()
                    lowerlips.showturtle()
                    screen.update()
                    sleep(0.1)
                openeyesr.hideturtle()
                closeeyes.showturtle()
                screen.update()
                sleep(0.1)
            elif count == 5:
                # open eyes 4 sec with rightcornea then blink
                closeeyes.hideturtle()
                openeyesr.showturtle()
                screen.update()
                for i in range(0, 20, 1):
                    upperlips.showturtle()
                    lowerlips.showturtle()
                    screen.update()
                    sleep(0.1)
                    upperlips.hideturtle()
                    lowerlips.showturtle()
                    screen.update()
                    sleep(0.1)
                openeyesr.hideturtle()
                closeeyes.showturtle()
                screen.update()
                sleep(0.1)
            elif count == 6:
                # open eyes 4 sec with leftcornea then blink
                closeeyes.hideturtle()
                openeyesl.showturtle()
                screen.update()
                for i in range(0, 20, 1):
                    upperlips.showturtle()
                    lowerlips.showturtle()
                    screen.update()
                    sleep(0.1)
                    upperlips.hideturtle()
                    lowerlips.showturtle()
                    screen.update()
                    sleep(0.1)
                openeyesl.hideturtle()
                closeeyes.showturtle()
                screen.update()
                sleep(0.1)
            elif count == 7:
                # open eyes 4 sec with leftcornea then blink
                closeeyes.hideturtle()
                openeyesl.showturtle()
                screen.update()
                for i in range(0, 20, 1):
                    upperlips.showturtle()
                    lowerlips.showturtle()
                    screen.update()
                    sleep(0.1)
                    upperlips.hideturtle()
                    lowerlips.showturtle()
                    screen.update()
                    sleep(0.1)
                openeyesl.hideturtle()
                closeeyes.showturtle()
                screen.update()
                sleep(0.1)
            else:
                # open eyes 4 sec with mid cornea then blink
                closeeyes.hideturtle()
                openeyesm.showturtle()
                screen.update()
                for i in range(0, 20, 1):
                    upperlips.showturtle()
                    lowerlips.showturtle()
                    screen.update()
                    sleep(0.1)
                    upperlips.hideturtle()
                    lowerlips.showturtle()
                    screen.update()
                    sleep(0.1)
                openeyesm.hideturtle()
                closeeyes.showturtle()
                screen.update()
                sleep(0.1)


def normalEmotion():
    __startEmotion()
    __showMouth()
    __showNose()
    __showEyeBrows()
    __blinkEyes()
    __endEmotion()

def normalTalkingEmotion():
    __startEmotion()
    __showEyeBrows()
    __showNose()
    __talkBlink()
    __endEmotion()


