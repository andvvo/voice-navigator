import whisper

model = whisper.load_model('tiny')
def transcribe(filename):
    result = whisper.transcribe(model, filename, fp16=False)
    return result['text']