import sys
from stt import record_and_transcribe, transcribe
from nlu import parse_intent
from automation import execute_command
from tts import speak

def main():

    print("============Voice Navigator Started============\n\n")

    try:
        print("----------Recording and Transcribing-----------")
        transcript = record_and_transcribe()
        if not transcript:
            print('No speech detected. Try again.\n')
            return
        print(f"[Transcript] {transcript}")
        print("-----------------------------------------------\n")

        print("----------Parsing Intent----------")
        intent = parse_intent(transcript)
        print(f"[Intent] {intent}")
        print("-----------------------------------\n")

        print(f"----------Executing Action----------")
        if (intent.confirmation_text):
            speak(intent.confirmation_text)
        execute_command(intent)
        print("--------------------------------------\n")

    except KeyboardInterrupt:
        print("Exiting Voice Navigator.")
        sys.exit(0)

if __name__ == '__main__':
    main()