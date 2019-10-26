"""
Code Link : https://www.instructables.com/id/Servo-Motor-Control-With-Raspberry-Pi/

***RASPBERRY PI PACKAGES***
    self >> sudo pip3 install self

***PYTHON INSTALLED PACKAGES***
   RPi.GPIO >> pip3 install RPi.GPIO def
"""
import self
from sys import exit
from enum import Enum
from DIO import DIO_PINS
from RPi import GPIO
from time import sleep

# Servo Channels Gives Ability to Access Connected SERVO_PINS
class CHANNELS(Enum):
    SERVO_1 = DIO_PINS.SERVO_1.value
    SERVO_2 = DIO_PINS.SERVO_2.value
    SERVO_3 = DIO_PINS.SERVO_3.value
    SERVO_4 = DIO_PINS.SERVO_4.value
    SERVO_5 = DIO_PINS.SERVO_5.value
    SERVO_6 = DIO_PINS.SERVO_6.value
    SERVO_7 = DIO_PINS.SERVO_7.value

class Servo:
    __servoChannel = 0
    __servoAngle = 0
    __servoPWM = 0
    __initFreq = 50  # Frequency = 50Hz

    # Initialize Channel According to Object Channel
    # SetChannel Which Object Gonna Control
    def __init__(self, selectedServoChannel):
        self.__servoChannel = selectedServoChannel
        GPIO.setup(selectedServoChannel, GPIO.OUT)
        self.__servoPWM = GPIO.PWM(selectedServoChannel, self.__initFreq)

    # Returns Object Channel
    def getChannel(self):
        return self.__servoChannel

    # Passed Object Angle into Angle Parameter
    def setAngle(self, servoAngle):
        if self.getChannel() == 0 :
            print("Channel Missed!")
            exit()
        else :
            self.__servoAngle = servoAngle

    # Returns Object Angle
    def getAngle(self):
        return self.__servoAngle

    # Passes Angle to PWM in DutyCycle Equation then Start Square Signal by Turning Object PIN (ON & OFF)
    def start(self):
        self.__servoPWM.start(0)
        dutyCycle = self.getAngle()/18+2
        GPIO.output(self.getChannel(), True)
        self.__servoPWM.ChangeDutyCycle(dutyCycle)
        sleep(1)
        GPIO.output(self.getChannel(), False)
        self.__servoPWM.ChangeDutyCycle(0)

    # Stops Generating PWM Signals
    def stop(self):
        self.__servoPWM.stop()

"""
***Usage Example***
    import SERVO
    Servo_1 = SERVO.Servo(SERVO.CHANNELS.SERVO_1.value)
    Servo_1.setAngle(90)
    Servo_1.start()
    Servo_1.setAngle(40)
    Servo_1.start()
    Servo_1.stop()
"""
