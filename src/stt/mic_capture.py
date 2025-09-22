from pynput import keyboard
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import threading
import sys
sys.path.append('../')
from config.audio import SAMPLE_RATE, CHANNELS, DATA_TYPE
from config.settings import FILENAME, HOTKEY

frames = []                         # Chunks of contiguous audio
isRecording = False                 # State flag for recording
stop_event = threading.Event()      # State flag for stopping thread

def start_recording():
    """Sets 'frames' to an empty array and 'isRecording' to True."""
    global frames, isRecording
    frames = []
    isRecording = True
    print("Recording...")

def stop_recording():
    """Sets 'isRecording' to False and writes audio from frames to file."""
    global isRecording
    isRecording = False
    print("\nRecording stopped.")
    if frames:
        audio = np.concatenate(frames, axis=0) # Combine chunks of audio
        write(FILENAME, SAMPLE_RATE, audio)
        print(f"Recording saved to {FILENAME}")

def on_press(key):
    """Start recording when 'SPACE' is pressed."""
    if key == keyboard.Key.space and not isRecording:
        start_recording()

def on_release(key):
    """Stop recording when 'SPACE' is released."""
    if key == keyboard.Key.space and isRecording:
        stop_recording()
        return False

def audio_stream():
    """
    Record chunks of audio continuously
    when 'isRecording' flag is True.
    """
    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype=DATA_TYPE
    ) as stream:
        while not stop_event.is_set():
            data, _ = stream.read(int(0.01 * SAMPLE_RATE))   # 0.1 sec chunks
            if isRecording:
                frames.append(data) # Record chunks of audio

def record():
    """
    Records audio while HOTKEY is held down.
    Stops when HOTKEY is released.
    """

    # Run audio capture in a background thread
    audio_thread = threading.Thread(target=audio_stream, daemon=True)
    audio_thread.start()

    print(f"Press and hold '{HOTKEY}' to record. Release to stop.")

    # Listen for key presses while audio is being captured
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    ) as listener:
        listener.join()

    stop_event.set()
    audio_thread.join()
    
    return FILENAME