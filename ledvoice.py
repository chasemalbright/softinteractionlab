import os
from unittest.mock import sentinel
from gpiozero import LED
import time




red = LED(23)
blue = LED(18)
yellow = LED(21)
green = LED(22)
white = LED(12)

def lit(color):
    color.on()
    time.sleep(1.2)
    color.off()

def speak(sentence):
    os.popen('espeak "' + sentence + '" --stdout | aplay 2> /dev/null').read()


sentence = "x"
while (sentence != "q"):
    sentence = input("Please enter a command << ")

    if (sentence.find("red") >= 0 or sentence.find("Red") >= 0):
        speak("Turning on red light")
        lit(red)
    if (sentence.find("blue") >= 0 or sentence.find("Blue") >= 0):
        speak("Turning on blue light")
        lit(blue)
    if (sentence.find("yellow") >= 0 or sentence.find("Yellow") >= 0):
        speak("Turning on yellow light")
        lit(yellow)
    if (sentence.find("green") >= 0 or sentence.find("Green") >= 0):
        speak("Turning on green light")
        lit(green)
    if (sentence.find("white") >= 0 or sentence.find("White") >= 0):
        speak("Turning on white light")
        lit(white)






