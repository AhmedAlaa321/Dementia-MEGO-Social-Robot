from RPi import GPIO
from MIC import Microphone
GPIO.setmode(GPIO.BOARD)
Microphone_obj = Microphone()
Microphone_obj.record()
GPIO.cleanup()
