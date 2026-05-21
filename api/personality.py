"""KAGUYA Personality API — Vercel Serverless."""
from http.server import BaseHTTPRequestHandler
import json

# Default personality traits (Big Five)
DEFAULT_TRAITS = {
    "openness": 0.75,
    "conscientiousness": 0.62,
    "extraversion": 0.71,
    "agreeableness": 0.78,
    "neuroticism": 0.34,
}

# In-memory store (serverless — resets on cold start)
_store = {"traits": DEFAULT_TRAITS.copy()}


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps({
            "profile_id": "default",
            "traits": _store["traits"],
            "version": "0.2.0",
        }).encode())

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length)) if length else {}
        
        if "traits" in body:
            for key, val in body["traits"].items():
                if key in _store["traits"]:
                    _store["traits"][key] = max(0.0, min(1.0, float(val)))
        
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps({
            "profile_id": "default",
            "traits": _store["traits"],
            "updated": True,
        }).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
