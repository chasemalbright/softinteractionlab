from flask import  Flask
from flask_ngrok import run_with_ngrok
from gpiozero import LED
from RpiMotorLib import RpiMotorLib
import RPi.GPIO as GPIO
import time

g1 = LED(12)
g2 = LED(16)
g3 = LED(19)
g4 = LED(21)

lightArray = [g1,g2,g3,g4]

count = 0

#################################STEPPERCODE##############################################
#define GPIO pins
direction= 24 # Direction (DIR) GPIO Pin
step = 23 # Step GPIO Pin
EN_pin = 22 # enable pin (LOW to enable)

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output

GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor

def motorCCW():
    mymotortest.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                     "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                     770, # number of steps
                     .0005, # step delay [sec]
                     False, # True = print verbose output 
                     .05) # initial delay [sec]


def motorCW():
    mymotortest.motor_go(True, # True=Clockwise, False=Counter-Clockwise
                     "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                     770, # number of steps
                     .0005, # step delay [sec]
                     False, # True = print verbose output 
                     .05) # initial delay [sec]
##########################################################################################

#helper functions
def lightOn(count):
    for i in range(count):
        lightArray[i].on()
    motorCW()

def lightOff(count):
    lightArray[count].off()
    motorCCW()

app = Flask(__name__)
run_with_ngrok(app)

#http routes

@app.route('/increment')
def increment():
    global count
    count= count+1
    lightOn(count)

@app.route('/decrement')
def decrement():
    global count
    if count == 0:
        count = 0
    else:
        count = count - 1
    lightOff(count)

@app.route('/reset')
def reset():
    global count
    count = 0
    for i in range(4): #FIXME
        lightArray[i].off()



if __name__ == "__main__":
    app.run()