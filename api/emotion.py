"""KAGUYA Emotion API — Vercel Serverless."""
from http.server import BaseHTTPRequestHandler
import json
import random

EMOTIONS = ["joy", "sadness", "anger", "fear", "surprise", "disgust", "trust", "anticipation", "neutral"]

EMOTION_ICONS = {
    "joy": " ", "sadness": " ", "anger": " ", "fear": " ",
    "surprise": " ", "disgust": " ", "trust": " ", "anticipation": " ", "neutral": " ",
}

_store = {
    "emotion": {
        "primary": "joy",
        "intensity": 0.72,
        "valence": 0.6,
        "arousal": 0.5,
        "icon": " ",
    }
}


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps({
            "profile_id": "default",
            "emotion": _store["emotion"],
        }).encode())

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length)) if length else {}

        if "event" in body:
            # Simulate emotion change based on event
            event = body["event"].lower()
            if any(w in event for w in ["happy", "good", "love", "great", "wonderful"]):
                _store["emotion"] = {"primary": "joy", "intensity": 0.85, "valence": 0.8, "arousal": 0.6, "icon": " "}
            elif any(w in event for w in ["sad", "bad", "miss", "lonely", "cry"]):
                _store["emotion"] = {"primary": "sadness", "intensity": 0.7, "valence": -0.5, "arousal": 0.3, "icon": " "}
            elif any(w in event for w in ["angry", "hate", "annoying", "stupid"]):
                _store["emotion"] = {"primary": "anger", "intensity": 0.75, "valence": -0.6, "arousal": 0.8, "icon": " "}
            elif any(w in event for w in ["surprise", "wow", "omg", "unexpected"]):
                _store["emotion"] = {"primary": "surprise", "intensity": 0.8, "valence": 0.3, "arousal": 0.9, "icon": " "}
            else:
                _store["emotion"] = {"primary": "neutral", "intensity": 0.5, "valence": 0.0, "arousal": 0.4, "icon": " "}

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps({
            "profile_id": "default",
            "emotion": _store["emotion"],
        }).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
