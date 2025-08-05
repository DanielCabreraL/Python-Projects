# --------------------------------- IMPORT LIBRARYS --------------------------------- #

import speech_recognition as sr # Converts what we say via audio to text
import pyttsx3 as pt            # Converts text to voice
import pywhatkit as pw          # Automations

# --------------------------------- ASSISTANT CONFIG --------------------------------- #
# Name of our assistant
name = "Pepa"

listener = sr.Recognizer()                              # Recognize our voice

engine = pt.init()                                      # We initialize pyttsx3

# Select the voice
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)              # Select Sabina voice (spanish)

# Pepa talk
def talk(text):
    engine.say(text) 
    engine.runAndWait()                                 # Convert 'text' to voice

# Pepa listen
def listen():
    try:
        with sr.Microphone() as source:                 # Take our microphone as a source to listen
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language = 'es')
            rec = rec.lower()
            if name in rec:                             # If we name Pepa in the audio
                rec = rec.replace(name, '')             # Replace the name for nothing        
    except:
        pass
    
    return rec

# --------------------------------- END ASSISTANT CONFIG --------------------------------- #