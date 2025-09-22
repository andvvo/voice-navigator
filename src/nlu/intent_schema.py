from pydantic import BaseModel, Field
from typing import Optional

class Parameters(BaseModel):
    """Various optional parameters for actions (url, text, recipient, etc.)."""
    url: Optional[str]
    subject: Optional[str]
    text: Optional[str]
    recipient: Optional[str]

class IntentCommand(BaseModel):
    """
    Generic schema for parsed voice commands.
    Covers most common actions (browser, typing, email, etc.)
    and allows future extensions.
    """

    # High level action
    action: str = Field(
        ...,
        description="Name of the action, e.g. 'open_browser', 'type_text', 'send_email', 'search_web'."
    )

    # Parameters for that action
    parameters: Parameters = Field(
        ...,
        description="Action specific arguments (e.g., url, text, subject, body, recipient)."
    )

    # Confirmation text for action
    confirmation_text: str = Field(
        ...,
        description="Phrase for TTS confirmation, e.g. 'Opening Google Docs.'"
    )