from .whisper_engine import transcribe
from .mic_capture import record

def record_and_transcribe():
    """
    Records audio while 'HOTKEY' is pressed and held down.
    Transcribes audio and returns transcription.
    """
    filename = record()
    return transcribe(filename)