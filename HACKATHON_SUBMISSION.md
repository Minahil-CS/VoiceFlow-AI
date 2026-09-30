# VoiceFlow AI — Hackathon Submission

## Project Title
VoiceFlow AI

## Tagline
Turn your voice into completed tasks.

## Short Description
VoiceFlow AI is a voice-first productivity agent that listens to natural spoken requests, converts them into structured tasks, detects priority and due-date hints, and lets users confirm and save the task without typing.

## Long Description
VoiceFlow AI addresses a simple productivity problem: people often know what they need to do but do not want to stop and type every task manually.

With VoiceFlow AI, the user speaks naturally. AssemblyAI provides the speech-to-text layer, and the application interprets the transcript into an actionable task. The interface presents the detected task, priority, and due-date hint for confirmation before saving it.

The prototype demonstrates a complete voice-first workflow: microphone input, real-time user feedback, AssemblyAI transcription, task understanding, confirmation, and task management.

The architecture is intentionally lightweight so the core voice interaction is easy to demonstrate and understand. Future versions can add calendar integration, multilingual support, recurring tasks, authentication, reminders, and cloud persistence.

## Technology Tags
AssemblyAI, Voice AI, Speech-to-Text, AI Agent, Python, Flask, JavaScript, NLP, Productivity

## Category
AI / Voice Agents / Productivity

## Key Innovation
Instead of treating voice as an alternative keyboard, VoiceFlow makes conversational voice the primary task-creation interface.

## Demo Flow
1. Open VoiceFlow AI.
2. Click the microphone.
3. Say: "Remind me tomorrow to submit my university form."
4. Stop recording.
5. AssemblyAI transcribes the request.
6. VoiceFlow extracts the task, priority and due-date hint.
7. User confirms.
8. The task appears in the task list.

## Future Scope
- Calendar and reminder integration
- Urdu/English multilingual support
- Recurring tasks
- Cloud synchronization
- Personalized task prioritization
- Voice commands for editing and completing tasks
