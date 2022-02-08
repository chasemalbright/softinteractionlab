import speech_recognition as sr
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        audio=r.listen(source)
        try:    
            query = r.recognize_google(audio)
            print(f"master:{query}")
            return query
        except:
            print("Try Again")