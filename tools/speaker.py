import pyttsx3


def speak(text, language):
    if language == "pt_br":
        engine = pyttsx3.init()
        engine.setProperty('voice', 'portuguese')
        engine.setProperty('rate', 165)
        engine.setProperty('volume', 1.9)
        engine.say(text)
        engine.runAndWait()
    elif language == "en_us":
        engine = pyttsx3.init()
        engine.setProperty('voice', 'english')
        engine.setProperty('rate', 165)
        engine.setProperty('volume', 1.9)
        engine.say(text)
        engine.runAndWait()
