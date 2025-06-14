import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 70)
    engine.say(text)
    engine.runAndWait()
