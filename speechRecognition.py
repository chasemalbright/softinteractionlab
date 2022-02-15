#imports and dependencies
import speech_recognition as sr
from gpiozero import LED
from time import sleep
import os

# initialize led interface
red = LED(23)

# audio inout variables
r = sr.Recognizer()
mic = sr.Microphone()

def speak(sentence):
    os.popen('espeak "' + sentence + '" --stdout | aplay 2> /dev/null').read()
speak("hello chase")
while True:
    with mic as source:
        audio = r.listen(source)
    words = r.recognize_google(audio)
    print(words)
    speak(words)
#
#
#
#
#   The pi has some configuration errors with audio input need to trouble shoot
#
#
#
#
#
