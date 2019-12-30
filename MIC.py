"""
Library Link : https://pypi.org/project/SpeechRecognition/

***RASPBERRY PI PACKAGES***
   FLAC >> sudo apt-get install flac

***PYTHON INSTALLED PACKAGES***
   PyAudio >> pip3 install pyaudio
   SpeechRecognition >> pip3 install SpeechRecognition
   PocketSphinx (For OFFLINE Recognition) >> python -m pip install --upgrade pip setuptools wheel,
                                             pip install --upgrade pocketsphinx
"""
import self
import speech_recognition as speechRecognition
from RPi import GPIO
from DIO import DIO_PINS

class Microphone:
    __LED_CHANNEL = DIO_PINS.MIC_LED.value
    __speechRecognizer = speechRecognition.Recognizer()

    def __init__(self):
        GPIO.setup(self.__LED_CHANNEL, GPIO.OUT)

    def __LED_ON(self):
        GPIO.output(self.__LED_CHANNEL, True)

    def __LED_OFF(self):
        GPIO.output(self.__LED_CHANNEL, False)

    #Enables Mic and Return Speech it disables Mic automatically
    def record(self):
        recognizedAudio = ""
        self.__LED_ON()
        with speechRecognition.Microphone() as micSource:
           recordedAudio = self.__speechRecognizer.listen(micSource)

        # ONLINE RECOGNIZER
        # Recognize Speech Using Google_Speech_Recognition
        try:
            recognizedAudio = self.__speechRecognizer.recognize_google(recordedAudio)
        except speechRecognition.UnknownValueError:
            print("Fail To Understand Audio!")
        except speechRecognition.RequestError:
            # OFFLINE RECOGNIZER
            try:
                recognizedAudio = self.__speechRecognizer.recognize_sphinx(recordedAudio)
            except speechRecognition.UnknownValueError:
                print("Fail To Understand Audio!")
            except speechRecognition.RequestError:
                print("Couldn't Recognize Audio!!")
        self.__LED_OFF()
        return recognizedAudio
"""
***Usage Example***
    from MIC import Microphone
    mic = Microphone()
    speechText = mic.record()
"""
