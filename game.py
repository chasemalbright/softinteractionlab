import logging
import os
import time
 
from flask import Flask
from flask_ask import Ask, request, session, question, statement
from gpiozero import LED

red = LED(23)


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@ask.launch
def launch():
    speech_text = 'Welcome to the American states quiz game.'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)


@ask.intent('QuizIntent')
def game():
    red.on()
    time.sleep(1)
    red.off()

@ask.session_ended
def session_ended():
    return "{}", 200
 
 
if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)