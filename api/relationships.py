"""KAGUYA Relationships API — Vercel Serverless."""
from http.server import BaseHTTPRequestHandler
import json

_store = {
    "relationships": [
        {"id": "user_001", "name": "User", "trust": 0.75, "affection": 0.68, "familiarity": 0.55, "interactions": 42},
    ]
}


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps({
            "profile_id": "default",
            "relationships": _store["relationships"],
        }).encode())

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length)) if length else {}

        if "name" in body:
            new_rel = {
                "id": f"user_{len(_store['relationships']) + 1:03d}",
                "name": body["name"],
                "trust": body.get("trust", 0.5),
                "affection": body.get("affection", 0.5),
                "familiarity": body.get("familiarity", 0.3),
                "interactions": 0,
            }
            _store["relationships"].append(new_rel)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps({
            "profile_id": "default",
            "relationships": _store["relationships"],
        }).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
