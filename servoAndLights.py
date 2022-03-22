from flask import  Flask
from flask_ngrok import run_with_ngrok
from gpiozero import LED, Servo
from time import sleep



servo = Servo(17)
servo.detach()

def spin():
    servo.min()
    sleep(4)
    servo.detach()

g1 = LED(12)
g2 = LED(16)
g3 = LED(19)
g4 = LED(21)

lightArray = [g1,g2,g3,g4]

count = 0

def lightOn(count):
    for i in range(count):
        lightArray[i].on()
    spin()

def lightOff(count):
    lightArray[count].off()


app = Flask(__name__)
run_with_ngrok(app)

#routes

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