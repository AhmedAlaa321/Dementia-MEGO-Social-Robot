"""
Link of Code : https://www.instructables.com/id/Servo-Motor-Control-With-Raspberry-Pi/
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

    def __initialize(self):
        GPIO.setup(self.getChannel(), GPIO.OUT)
        self.__servoPWM = GPIO.PWM(self.getChannel(), self.__initFreq)

    def setChannel(self, selectedServoChannel):
        self.__servoChannel = selectedServoChannel
        self.__initialize()

    def getChannel(self):
        return self.__servoChannel

    def setAngle(self, servoAngle):
        if self.getChannel() == 0 :
            print("Channel Missed!")
            exit()
        else :
            self.__servoAngle = servoAngle

    def getAngle(self):
        return self.__servoAngle

    def start(self):
        self.__servoPWM.start(0)
        dutyCycle = self.getAngle()/18+2
        GPIO.output(self.getChannel(), True)
        self.__servoPWM.ChangeDutyCycle(dutyCycle)
        sleep(1)
        GPIO.output(self.getChannel(), False)
        self.__servoPWM.ChangeDutyCycle(0)

    def stop(self):
        self.__servoPWM.stop()
