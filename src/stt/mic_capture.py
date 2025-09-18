import sounddevice as sd
from scipy.io.wavfile import write
from config.audio import SAMPLE_RATE, CHANNELS, DURATION, DATA_TYPE
from config.settings import FILENAME

def listen():
    print('Listening...')
    audio = sd.rec(frames=int(SAMPLE_RATE * DURATION),
                   samplerate=SAMPLE_RATE,
                   channels=CHANNELS,
                   dtype=DATA_TYPE)
    sd.wait()
    write(FILENAME, SAMPLE_RATE, audio)
    return FILENAME