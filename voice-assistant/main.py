# --------------------------------- IMPORT LIBRARYS --------------------------------- #

import speech_recognition as sr # Converts what we say via audio to text
import pyttsx3 as pt            # Converts text to voice
import pywhatkit as pw          # Automations
import pepa_functions as fun    # Pepa functions

# ------------------------------------ RUN PEPA ------------------------------------ #
if __name__ == '__main__':
    fun.run_pepa()