"""KAGUYA Chat API — Vercel Serverless."""
from http.server import BaseHTTPRequestHandler
import json
import random
import time

PERSONALITY_RESPONSES = {
    "joy": [
        "That makes me so happy!  ",
        "Wonderful! I'm feeling great about this!",
        "Yay! This is amazing!",
    ],
    "neutral": [
        "I see. Tell me more about that.",
        "Interesting perspective.",
        "Hmm, I understand.",
    ],
    "curiosity": [
        "Oh? That's fascinating! Tell me more!",
        "I'm really curious about this!",
        "What an interesting thought!",
    ],
}


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length)) if length else {}
        
        message = body.get("message", "")
        emotion = body.get("emotion", "neutral")
        
        # Generate personality-aware response
        responses = PERSONALITY_RESPONSES.get(emotion, PERSONALITY_RESPONSES["neutral"])
        response_text = random.choice(responses)
        
        # Add context based on message keywords
        msg_lower = message.lower()
        if any(w in msg_lower for w in ["hello", "hi", "hey", "halo"]):
            response_text = random.choice([
                "Hello there! Nice to meet you!  ",
                "Hi! I'm KAGUYA, your AI personality companion!",
                "Hey! How can I help you today?",
            ])
        elif any(w in msg_lower for w in ["who are you", "what are you"]):
            response_text = "I'm KAGUYA, an AI Personality Engine! I have emotions, relationships, and I can evolve over time. Nice to meet you!"
        elif any(w in msg_lower for w in ["how are you", "how do you feel"]):
            response_text = f"I'm feeling {emotion} right now! Thanks for asking!  "
        
        result = {
            "response": response_text,
            "emotion": emotion,
            "tone": {
                "warmth": 0.78,
                "humor": 0.65,
                "formality": 0.42,
                "verbosity": 0.55,
            },
            "timestamp": time.time(),
        }
        
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
