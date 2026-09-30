# VoiceFlow AI

VoiceFlow AI is a voice-first productivity agent built for the AssemblyAI Voice Agent Hackathon.

## Core idea

Users speak naturally instead of typing tasks. AssemblyAI converts speech to text, and VoiceFlow turns the transcript into a structured task with priority and due-date hints.

## Features

- Browser microphone recording
- AssemblyAI speech-to-text integration
- Natural-language task capture
- Priority detection
- Due-date hint detection
- Confirmation before adding a task
- Local task history
- Simple responsive UI

## Run locally

### 1. Install Python

Python 3.11+ is recommended.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure AssemblyAI

Copy `.env.example` to `.env` and add your AssemblyAI API key:

```env
ASSEMBLYAI_API_KEY=your_key_here
```

### 4. Start

```bash
python app.py
```

Open:

http://127.0.0.1:5000

## Example voice commands

- "Remind me tomorrow to submit my university form."
- "Add a high priority task to finish my project today."
- "Remind me Friday to prepare the presentation."

## Hackathon positioning

VoiceFlow is intentionally voice-first: speech is the primary input and the system transforms conversational speech into an actionable workflow.

## Technology

- Python
- Flask
- AssemblyAI
- JavaScript
- HTML/CSS
- Browser MediaRecorder API
- LocalStorage

## Note

This prototype stores tasks locally in the browser. It is designed as a hackathon MVP and can later be extended with calendar integrations, authentication, multilingual voice support, recurring tasks, and external databases.
