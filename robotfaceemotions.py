import turtle
turtle.Turtle()
turtle.hideturtle()
turtle.setup(800,484)
screen.bgcolor("cyan")

def normalemotion():
   turtle.reset()
   turtle.fillcolor("black")
   turtle.speed(0)
   turtle.begin_fill()
   turtle.setpos(30,0)
   circle1 = turtle.circle(20)
   register_shape("righteye",circle1)
   turtle.setpos(-30,0)
   circle2 = turtle.circle(20)
   register_shape("lefteye",circle2)
   turtle.setpos(0,-50)
   rmouth= turtle.circle(40,-180)
   register_shape("mouth",rmouth)
   turtle.end_fill()
   screen.delay(1000)
   start1 = 40
   stop1 = 0
   step1 = -2
   for x in range(start1,stop1,step1):
      turtle.shape("righteye")
      turtle.resizemode("user")
      turtle.shapesize(start1)
      tuttle.shape("lefteye")
      turtle.resizemode("user")
      turtle.shapesize(start1)
      turtle.shape("mouth")
      turtle.resizemode("user")
      turtle.shapesize(start1)
      screen.delay(100)
   start2 = 0
   stop2 = 40
   step2 = 2
   for x in xrange(start2,stop2,step2):
      turtle.shape("righteye")
      turtle.resizemode("user")
      turtle.shapesize(start2)
      tuttle.shape("lefteye")
      turtle.resizemode("user")
      turtle.shapesize(start2)
      turtle.shape("mouth")
      turtle.resizemode("user")
      turtle.shapesize(start2)
      screen.delay(100)

       


def main():
     
     while 1:
        normalemotion()
      

main()

turtle.done()

    
