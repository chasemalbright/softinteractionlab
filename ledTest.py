from gpiozero import LED
import time

red = LED(23)
blue = LED(18)

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