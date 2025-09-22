import yagmail
from tts import speak

contacts = {
    "andy" : "andy.vo@berkeley.edu"
}

def send_email(subject="", text="", recipient=""):
    with yagmail.SMTP("python.script837@gmail.com", oauth2_file="~/oauth2_creds.json") as yag:
        result = yag.send(
            to=contacts[recipient.lower()],
            subject=subject,
            contents=text
        )

        if not result:
            print("Email sent.")
            speak("Email sent.")
        else:
            print("Unable to send email.")
            speak("Unable to send email.")