import pyttsx3

def Speak(text ):
    engine = pyttsx3.init()
    engine.setProperty('rate',190)
    engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    engine.say(text)
    engine.runAndWait()
