from openai import OpenAI
from .intent_schema import IntentCommand

client = OpenAI()

def parse_intent(text):
    """
    Parses intent from 'text' using GPT-5-nano.
    Outputs intent as 'IntentCommand' JSON schema.
    """
    response = client.responses.parse(
        model="gpt-5-nano",
        input= [
            {
                "role" : "system",
                "content" : (
                    "Extract the user's intent as an action and parameters "
                    "based on the schema provided. Fill all required fields."
                    "Do not add more context than what was provided."
                    "Do not provide fill in the blanks, e.g. '[Time]'"
                    )
            },
            {
                "role" : "user",
                "content" : text
            }
        ],
        text_format=IntentCommand
    )

    return response.output_parsed