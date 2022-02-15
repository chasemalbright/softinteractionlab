from flask import  Flask
from flask_ngrok import run_with_ngrok
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

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/redon')
def redon():
    red.on()
    #return render_template('on.html')

@app.route('/redoff')
def redoff():
    red.off()
    #return render_template('./page.html')

@app.route('/whiteon')
def whiteon():
    white.on()
    #return render_template('on.html')

@app.route('/whiteoff')
def whiteoff():
    white.off()
    #return render_template('./page.html')

@app.route('/blueon')
def blueon():
    blue.on()
    #return render_template('on.html')

@app.route('/blueoff')
def blueoff():
    blue.off()
    #return render_template('./page.html')

if __name__ == "__main__":
    app.run()