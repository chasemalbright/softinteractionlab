from gpiozero import LED
import time

red = LED(23)
blue = LED(18)
yellow = LED(21)
green = LED(22)
white = LED(12)

color = "x"
while(color != "q"):
    color = input("enter color, q to end << ")
    if (color =='r'):
        red.on()
        time.sleep(1)
        red.off()
    if (color == 'b'):
        blue.on()
        time.sleep(1)
        blue.off()
    if (color == 'y'):
        yellow.on()
        time.sleep(1)
        yellow.off()
    if (color == 'g'):
        green.on()
        time.sleep(1)
        green.off()
    if (color == 'w'):
        white.on()
        time.sleep(1)
        white.off()