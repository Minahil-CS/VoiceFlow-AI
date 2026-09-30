import os
import tempfile
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import assemblyai as aai

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure AssemblyAI API key
API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
if not API_KEY:
    raise ValueError("ASSEMBLYAI_API_KEY not found. Check your .env file.")

aai.settings.api_key = API_KEY

@app.route("/")
def index():
    return render_template("index.html")

@app.post("/api/transcribe")
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file received"}), 400

    audio = request.files["audio"]

    # Use a unique temporary file per request
    temp_fd, temp_path = tempfile.mkstemp(suffix=".webm")

    try:
        # Close file descriptor to write with flask file object safely
        os.close(temp_fd)
        audio.save(temp_path)

        # File size check (< 2KB check)
        if os.path.getsize(temp_path) < 2000:
            return jsonify({"error": "Audio file is too short or empty. Please speak again."}), 400

        # Enable automatic language detection
        config = aai.TranscriptionConfig(
            language_detection=True
        )

        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(temp_path, config=config)

        if transcript.status == aai.TranscriptStatus.error:
            return jsonify({"error": transcript.error}), 500

        text = (transcript.text or "").strip()
        if not text:
            return jsonify({"error": "I couldn't understand any speech. Please speak clearly and try again."}), 400

        return jsonify({"text": text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        # Guarantee temp file cleanup
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    app.run(debug=True)