import whisper

model = whisper.load_model('tiny')

def transcribe(filename):
    """Transcribes audio from 'filename' and returns transcription."""
    result = whisper.transcribe(model, filename, fp16=False)
    return result['text']