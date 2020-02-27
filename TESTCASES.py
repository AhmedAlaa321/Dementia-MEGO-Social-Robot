import tkinter as tk
from MIC import Microphone
import Speaker
from RPi import GPIO
import SERVO
from time import sleep
#import LCD
from Camera import Camera

#initializations
#initializing GUI
window = tk.Tk()
window.title("Unit Test") #setting Title For Window
window.geometry("800x500")
#initializing Speaker and microphone
mic = Microphone()
cam = Camera()
speakerObj = Speaker.Speaker()
speakerObj.setSpeechRate(150)
#initializing LCD
#LCD.initialize()
speakerObj.setVolume(100)
speakerObj.say("please choose any thing you want to test")

class Servo:
    def neckServoMove():
         speakerObj.setVolume(100)
         speakerObj.say("Rotating Right")
         GPIO.setmode(GPIO.BOARD)
         Servo_1 = SERVO.Servo(SERVO.CHANNELS.SERVO_3.value)
         Servo_1.setAngle(100)
         Servo_1.start()
         speakerObj.setVolume(100)
         speakerObj.say("Rotating Left")
         Servo_1.setAngle(189)
         Servo_1.start()
         Servo_1.stop()
         GPIO.cleanup()

    def neckServoMoveRight():
         GPIO.setmode(GPIO.BOARD)
         Servo_1 = SERVO.Servo(SERVO.CHANNELS.SERVO_3.value)
         Servo_1.setAngle(100)
         Servo_1.start()
         Servo_1.stop()
         GPIO.cleanup()

    def neckServoMoveLeft():
         GPIO.setmode(GPIO.BOARD)
         Servo_1 = SERVO.Servo(SERVO.CHANNELS.SERVO_3.value)
         Servo_1.setAngle(189)
         Servo_1.start()
         Servo_1.stop()
         GPIO.cleanup()

    def RightShoulderServoFirstDegreeMove():
        speakerObj.setVolume(100)
        speakerObj.say("Front UP")
        GPIO.setmode(GPIO.BOARD)
        Servo_1 = SERVO.Servo(SERVO.CHANNELS.SERVO_2.value)
        Servo_1.setAngle(0)
        Servo_1.start()
        speakerObj.setVolume(100)
        speakerObj.say("Back Down")
        Servo_1.setAngle(90)
        Servo_1.start()
        Servo_1.stop()
        GPIO.cleanup()

    def RightShoulderServoSecondDegreeMove():
        speakerObj.setVolume(100)
        speakerObj.say("Right UP")
        GPIO.setmode(GPIO.BOARD)
        Servo_1 = SERVO.Servo(SERVO.CHANNELS.SERVO_4.value)
        Servo_1.setAngle(0)
        Servo_1.start()
        speakerObj.setVolume(100)
        speakerObj.say("left Down")
        Servo_1.setAngle(90)
        Servo_1.start()
        Servo_1.stop()
        GPIO.cleanup()

    def LeftShoulderServoFirstDegreeMove():
        speakerObj.setVolume(100)
        speakerObj.say("Front UP")
        GPIO.setmode(GPIO.BOARD)
        Servo_1 = SERVO.Servo(SERVO.CHANNELS.SERVO_6.value)
        Servo_1.setAngle(0)
        Servo_1.start()
        speakerObj.setVolume(100)
        speakerObj.say("Back Down")
        Servo_1.setAngle(90)
        Servo_1.start()
        Servo_1.stop()
        GPIO.cleanup()

    def LeftShoulderServoSecondDegreeMove():
        speakerObj.setVolume(100)
        speakerObj.say("Left UP")
        GPIO.setmode(GPIO.BOARD)
        Servo_1 = SERVO.Servo(SERVO.CHANNELS.SERVO_5.value)
        Servo_1.setAngle(0)
        Servo_1.start()
        speakerObj.setVolume(100)
        speakerObj.say("right Down")
        Servo_1.setAngle(90)
        Servo_1.start()
        Servo_1.stop()
        GPIO.cleanup()

    def LeftElbowMove():
        speakerObj.setVolume(100)
        speakerObj.say("moving UP")
        GPIO.setmode(GPIO.BOARD)
        Servo_1 = SERVO.Servo(SERVO.CHANNELS.SERVO_7.value)
        Servo_1.setAngle(0)
        Servo_1.start()
        speakerObj.setVolume(100)
        speakerObj.say("moving Down")
        Servo_1.setAngle(90)
        Servo_1.start()
        Servo_1.stop()
        GPIO.cleanup()

    def rightElbowMove():
        speakerObj.setVolume(100)
        speakerObj.say("moving UP")
        GPIO.setmode(GPIO.BOARD)
        Servo_1 = SERVO.Servo(SERVO.CHANNELS.SERVO_1.value)
        Servo_1.setAngle(0)
        Servo_1.start()
        speakerObj.setVolume(100)
        speakerObj.say("moving Down")
        Servo_1.setAngle(90)
        Servo_1.start()
        Servo_1.stop()
        GPIO.cleanup()


class Mic:
    def speechRecognition():
        speakerObj.setVolume(100)
        speakerObj.say("please check that the mic is turned on")
        sleep(2)
        speakerObj.say("please check that the battery is not empty")
        sleep(3)
        speakerObj.say("Say something to Test mic")
        sleep(3)
        speechText = mic.record()
        speakerObj.say("you have said")
        speakerObj.say(speechText)
        print("you have said ")
        print(speechText)
        speakerObj.say("Don't forget to close the mic after testing")

    def chatPot():
        speakerObj.setVolume(100)
        speakerObj.say("please check that the mic is turned on")
        speakerObj.say("please check that the battery is not empty")

class SpeakerTest():
    def textToSpeech():
        speakerObj.setVolume(10)
        speakerObj.say("setting Low volume")
        speakerObj.setVolume(50)
        speakerObj.say("setting medium volume")
        speakerObj.setVolume(100)
        speakerObj.say("setting High Volume")


class CameraTest:
    def faceRecognition():
        count = 0
        counter1 = 15
        counter2 = 30

        while 1:
            names, foundFace = cam.recognizeFaces()
            print(foundFace)

            if (foundFace == 0):
                if(count < counter1):
                    print("no move")
                elif(count == counter1):
                    print("move Right")
                    Servo.neckServoMoveRight()
                    sleep(2)
                elif(count < counter2):
                    print("no Move")
                elif(count == counter2):
                    print("move Left")
                    Servo.neckServoMoveLeft()
                    sleep(2)
                    count = 0

                count = count + 1

            elif (foundFace == 1):
                count = 0
                for nameIndex in range(len(names)):
                    name = names[nameIndex]
                    print("Found a face")
                    print(name)
                    speakerObj.say("hello")
                    speakerObj.say(name)

def testServo():
    Test1 = servoList.get()
    if (Test1 == "NeckServo"):
        Servo.neckServoMove()

    elif (Test1== "RightShoulderServoFirstDegree"):
        Servo.RightShoulderServoFirstDegreeMove()

    elif (Test1 == "RightShoulderServoSecondDegree"):
        Servo.RightShoulderServoSecondDegreeMove()

    elif (Test1 == "LeftShoulderServoFirstDegree"):
        Servo.LeftShoulderServoFirstDegreeMove()

    elif (Test1 == "LeftShoulderServoSecondDegree"):
        Servo.LeftShoulderServoSecondDegreeMove()

    elif (Test1 == "LeftElbow"):
        Servo.LeftElbowMove()

    elif (Test1 == "RightElbow"):
        Servo.rightElbowMove()

def testMic():
    Test2 = micList.get()
    if(Test2 == "SpeechRecognition" ):
        Mic.speechRecognition()

    elif(Test2 == "ChatPot"):
        Mic.chatPot()

def testCamera():
    Test3 = cameraList.get()
    window.withdraw()
    if(Test3 == "FaceRecognition"):
        CameraTest.faceRecognition()
        window.update()
        window.deiconify()

def testSpeaker():
    Test4 = speakerList.get()
    if(Test4 == "TextToSpeech"):
        SpeakerTest.textToSpeech()


#making Label for servo Test in coordinates (x,y)
servoLabel = tk.Label(window, text="Servos")
servoLabel.place(x=0, y=20, width=120, height=40)
servoLabel.configure(font=("Arial", 25))

#making Menu For Servo Testing
servoList = tk.Spinbox(window, values=("NeckServo", "RightShoulderServoFirstDegree", "RightShoulderServoSecondDegree", "LeftShoulderServoFirstDegree", "LeftShoulderServoSecondDegree", "RightElbow", "LeftElbow"))
servoList.place(x=10, y=80, width=350, height=40)
servoList.configure(font=("SANS", 14))

#making Button For Testing Servo
servosButton = tk.Button(window, text="TestServo", bg='blue', command=testServo)
servosButton.place(x=100, y=140, width=100, height=40)
servosButton.configure(font=("Helvetica", 15))

#making Label for mic Test in coordinates (x,y)
micLabel = tk.Label(window, text="MIC")
micLabel.place(x=470, y=20, width=120, height=40)
micLabel.configure(font=("Arial", 25))

#making Menu For Mic Testing
micList = tk.Spinbox(window, values=("SpeechRecognition", "ChatPot","DataBaseLink"))
micList.place(x=500, y=80, width=260, height=40)
micList.configure(font=("SANS", 14))

#making Button For Testing Mic
micButton = tk.Button(window, text="TestMic", bg='blue', command=testMic)
micButton.place(x=570, y=140, width=100, height=40)
micButton.configure(font=("Helvetica", 15))

#making Label for Camera Test in coordinates (x,y)
cameraLabel = tk.Label(window, text="Camera")
cameraLabel.place(x=0, y=200, width=120, height=40)
cameraLabel.configure(font=("Arial", 25))

#making Menu For Camera Testing
cameraList = tk.Spinbox(window, values=("FaceRecognition"))
cameraList.place(x=10, y=260, width=260, height=40)
cameraList.configure(font=("SANS", 14))

#making Button For Testing Camera
camButton = tk.Button(window, text="TestCAM", bg='blue', command=testCamera)
camButton.place(x=100, y=320, width=100, height=40)
camButton.configure(font=("Helvetica", 15))


#making Label for speaker Test in coordinates (x,y)
speakerLabel = tk.Label(window, text="SPEAKER")
speakerLabel.place(x=490, y=200, width=160, height=40)
speakerLabel.configure(font=("Arial", 25))

#making Menu For Speaker Testing
speakerList = tk.Spinbox(window, values=("TextToSpeech"))
speakerList.place(x=500, y=260, width=260, height=40)
speakerList.configure(font=("SANS", 14))

#making Button For Testing speaker
speakerButton = tk.Button(window, text="TestSpeaker", bg='blue',command=testSpeaker)
speakerButton.place(x=570, y=320, width=120, height=40)
speakerButton.configure(font=("Helvetica", 15))


window.mainloop()





