"""
Library Link : https://pypi.org/project/pyttsx3/
***RASPBERRY PI PACKAGES***
   Espeak >> sudo apt-get install espeak

***PYTHON INSTALLED PACKAGES***
   Pyttsx3 >> pip3 install pyttsx3
"""
import self
import pyttsx3

class Speaker :
    __speakerEngine = 0
    __RATE_KEY = 'rate'
    __VOLUME_KEY = 'volume'
    __VOICE_KEY = 'voice'
    __VOICE_ARRAY_KEY = 'voices'

    def __init__(self):
        self.__speakerEngine = pyttsx3.init()
        self.setSpeechVoice(25)

    def setSpeechRate(self, rate):
        self.__speakerEngine.setProperty(self.__RATE_KEY, rate)

    def getSpeechRate(self):
        return self.__speakerEngine.getProperty(self.__RATE_KEY)

    def setVolume(self, volume):
        self.__speakerEngine.setProperty(self.__VOLUME_KEY, (volume/100))

    def getVolume(self):
        return (self.__speakerEngine.getProperty(self.__VOLUME_KEY)*100)

    def setSpeechVoice(self, voiceNum):
        voiceArray = self.__getSpeechVoice()
        self.__speakerEngine.setProperty(self.__VOICE_KEY, voiceArray[voiceNum].id)

    def __getSpeechVoice(self):
        return self.__speakerEngine.getProperty(self.__VOICE_ARRAY_KEY)

    def say(self, text):
        self.__speakerEngine.say(text)
        self.__speakerEngine.runAndWait()
        self.__speakerEngine.stop()
