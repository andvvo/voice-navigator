from .whisper_engine import transcribe
from .mic_capture import listen

def listen_and_transcribe():
    filename = listen()
    return transcribe(filename)