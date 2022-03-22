# # Import libraries
# import RPi.GPIO as GPIO
# import time

# # Set GPIO numbering mode
# GPIO.setmode(GPIO.BCM)

# # Set pin 11 as an output, and define as servo1 as PWM pin
# GPIO.setup(17,GPIO.OUT)
# servo1 = GPIO.PWM(17,50) # pin 11 for servo1, pulse 50Hz

# # Start PWM running, with value of 0 (pulse off)
# servo1.start(0)

# # Loop to allow user to set servo angle. Try/finally allows exit
# # with execution of servo.stop and GPIO cleanup :)

# try:
#     while True:
#         #Ask user for angle and turn servo to it
#         angle = float(input('Enter angle between 0 & 180: '))
#         servo1.ChangeDutyCycle(2+angle)
#         time.sleep(0.5)
#         servo1.ChangeDutyCycle(0)

# finally:
#     #Clean things up at the end
#     servo1.stop()
#     GPIO.cleanup()
#     print("Servo Stop")



########################################################################################
# Import libraries
# import RPi.GPIO as GPIO
# import time

# # Set GPIO numbering mode
# GPIO.setmode(GPIO.BCM)

# # Set pin 11 as an output, and set servo1 as pin 11 as PWM
# GPIO.setup(17,GPIO.OUT)
# servo1 = GPIO.PWM(17,50) # Note 11 is pin, 50 = 50Hz pulse

# #start PWM running, but with value of 0 (pulse off)
# servo1.start(0)
# print ("Waiting for 2 seconds")
# time.sleep(2)

# #Let's move the servo!
# print ("Rotating 180 degrees in 10 steps")

# # Define variable duty
# duty = 2

# # Loop for duty values from 2 to 12 (0 to 180 degrees)
# while duty <= 12:
#     servo1.ChangeDutyCycle(duty)
#     time.sleep(.3)
#     servo1.ChangeDutyCycle(0)
#     time.sleep(.7)
#     duty = duty + 1

# # Wait a couple of seconds
# time.sleep(2)

# # Turn back to 90 degrees
# print ("Turning back to 90 degrees for 2 seconds")
# servo1.ChangeDutyCycle(7)
# time.sleep(2)

# #turn back to 0 degrees
# print ("Turning back to 0 degrees")
# servo1.ChangeDutyCycle(2)
# time.sleep(0.5)
# servo1.ChangeDutyCycle(0)

# #Clean things up at the end
# servo1.stop()
# GPIO.cleanup()
# print ("Servo STPO")

##############################################

# from Tkinter import *
# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(17, GPIO.OUT)
# pwm = GPIO.PWM(17, 100)
# pwm.start(5)

# class App:

#     def __init__(self, master):
#         frame = Frame(master)
#         frame.pack()
#         scale = Scale(frame, from_=0, to=180,
#               orient=HORIZONTAL, command=self.update)
#         scale.grid(row=0)


#     def update(self, angle):
#         duty = float(angle) / 10.0 + 2.5
#         pwm.ChangeDutyCycle(duty)

# root = Tk()
# root.wm_title('Servo Control')
# app = App(root)
# root.geometry("200x50+0+0")
# root.mainloop()

####################################################

# # Import libraries
# import RPi.GPIO as GPIO
# import time

# # Set GPIO numbering mode
# GPIO.setmode(GPIO.BCM)

# # Set pin 11 as an output, and set servo1 as pin 11 as PWM
# GPIO.setup(17,GPIO.OUT)
# servo1 = GPIO.PWM(17,50) # Note 11 is pin, 50 = 50Hz pulse

# #start PWM running, but with value of 0 (pulse off)
# servo1.start(0)
# print ("Waiting for 2 seconds")
# time.sleep(2)

# #Let's move the servo!
# print ("Rotating 180 degrees in 10 steps")

# # Define variable duty
# # duty = 2

# # # Loop for duty values from 2 to 12 (0 to 180 degrees)
# # while duty <= 12:
# #     servo1.ChangeDutyCycle(duty)
# #     time.sleep(1)
# #     duty = duty + 1

# def spin():
#     # Define variable duty
#     duty = 2

#     # Loop for duty values from 2 to 12 (0 to 180 degrees)
#     while duty <= 12:
#         servo1.ChangeDutyCycle(duty)
#         time.sleep(1)
#         duty = duty + 1
    

# x = 3
# if x > 2:
#     spin()

# y = 'w'
# if y == 'w':
#     spin()
# # Wait a couple of seconds
# # time.sleep(2)

# # # Turn back to 90 degrees
# # print ("Turning back to 90 degrees for 2 seconds")
# # servo1.ChangeDutyCycle(7)
# # time.sleep(2)

# # #turn back to 0 degrees
# # print ("Turning back to 0 degrees")
# # servo1.ChangeDutyCycle(2)
# # time.sleep(0.5)
# # servo1.ChangeDutyCycle(0)

# #Clean things up at the end
# servo1.stop()
# GPIO.cleanup()
# print ("Servo STPO")

######################################################

from gpiozero import Servo
from time import sleep
 
myGPIO=17
 
servo = Servo(myGPIO)
 
# while True:
# servo.mid()
# print("mid")
# sleep(0.5)
# servo.min()
# print("min")
# sleep(1)
# servo.mid()
# print("mid")
# sleep(0.5)
# servo.max()
# print("max")
# sleep(1)

def spin():
    servo.value = 1

spin()
print("hellofwfwe")
