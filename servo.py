import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(16, True)

#iemand anders 500
p = GPIO.PWM(16, 5000)

def SpinMotor(direction, num_steps):
    p.ChangeFrequency(5000)
    GPIO.output(18, direction)
    while num_steps > 0:
        p.start(1)
        time.sleep(0.01)
        num_steps -= 1
    p.stop()
    GPIO.cleanup()
    return True

direction_input = input('Please enter O or C fro Open or Close:')
num_steps = int(input('Please enter the number of steps: '))
if direction_input == 'C':
    SpinMotor(False, num_steps)
else:
    SpinMotor(True, num_steps)