# --------------------------------- IMPORT LIBRARYS --------------------------------- #

import speech_recognition as sr # Converts what we say via audio to text
import pyttsx3 as pt            # Converts text to voice
import pywhatkit as pw          # Automations
import pepa_config as conf      # Pepa config
import wikipedia                # Information from Wikipedia

# --------------------------------- ASSISTANT FUNCTIONS ---------------------------------- #
def run_pepa():
    rec = conf.listen()
    
    # ------------------------------ PLAY MUSIC ON YOUTUBE ------------------------------- #
    if ('reproducí'in rec or 'reproduce' in rec):
        music = rec.replace('reproducí' or 'reproduce', '')
        print("Reproduciendo " + music)
        conf.talk("Reproduciendo " + music)
        pw.playonyt(music)
    
    # ------------------------ SEARCH INFORMATION FROM WIKIPEDIA -------------------------- #
    elif ('busca' in rec or 'buscá' in rec):
        search = rec.replace('busca' or 'buscá', '')
        wikipedia.set_lang('es')                            # Information in Spanish
        wiki = wikipedia.summary(search, 1)                 # Summarize the information in 1 sentence
        print(search + ": " + wiki)                         # Presentation of information
        conf.talk(wiki)
    
    # Adding more funcs...
    
# ------------------------------- END ASSISTANT FUNCTIONS -------------------------------- #