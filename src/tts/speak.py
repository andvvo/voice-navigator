from gtts import gTTS
from playsound3 import playsound

def speak(text):
    tts = gTTS(text, lang='en')
    tts.save('output.mp3')
    playsound("./output.mp3")