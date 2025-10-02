# Voice Navigator

An AI-powered voice assistant designed to help motor-impaired individuals perform digital tasks through natural voice commands.

## Overview

Voice Navigator is an accessibility-focused application that enables users with motor impairments to control their computer and perform various digital tasks using only their voice. The system leverages advanced speech recognition, natural language understanding, and text-to-speech technologies to provide a seamless hands-free computing experience.

## Features

- **Voice-Activated Control**: Perform tasks using natural voice commands
- **Speech Recognition**: Powered by Whisper for accurate transcription
- **Natural Language Understanding**: Intelligent intent parsing to understand user commands
- **Text-to-Speech Feedback**: Audible responses to confirm actions and provide feedback
- **System Automation**: Control various system functions hands-free
- **Web Automation**: Navigate and interact with web content using voice commands

## Architecture

The project is organized into modular components:

- **STT (Speech-to-Text)**: Captures audio input and transcribes speech using Whisper
- **NLU (Natural Language Understanding)**: Parses user intent from transcribed text
- **Automation**: Executes system commands and web automation tasks
- **TTS (Text-to-Speech)**: Provides audio feedback to the user
- **Config**: Centralized configuration and settings management

## Installation

1. Clone the repository:

```bash
git clone https://github.com/andvvo/voice-navigator.git
cd voice-navigator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the voice assistant:

```bash
python src/main.py
```

Speak your commands naturally, and the assistant will transcribe, interpret, and execute them while providing audio feedback.

## Requirements

See `requirements.txt` for the full list of dependencies.

## Project Structure

```
src/
├── main.py              # Main application entry point
├── stt/                 # Speech-to-text module
├── nlu/                 # Natural language understanding
├── automation/          # Task automation and execution
├── tts/                 # Text-to-speech feedback
└── config/              # Configuration management
```

## Accessibility

This project is specifically designed to improve digital accessibility for individuals with motor impairments, enabling them to:

- Navigate their computer without physical input devices
- Execute complex tasks through simple voice commands
- Receive audio confirmation of actions
- Maintain independence in digital environments
