"""KAGUYA Memory API — Vercel Serverless."""
from http.server import BaseHTTPRequestHandler
import json
import time

_store = {
    "memories": [
        {
            "id": "mem_001",
            "content": "First interaction with the user",
            "importance": 0.8,
            "emotional_valence": 0.7,
            "timestamp": time.time() - 86400,
            "type": "episodic",
        },
        {
            "id": "mem_002",
            "content": "User asked about personality engine capabilities",
            "importance": 0.6,
            "emotional_valence": 0.3,
            "timestamp": time.time() - 3600,
            "type": "semantic",
        },
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
            "memories": _store["memories"],
            "total": len(_store["memories"]),
        }).encode())

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length)) if length else {}

        if "content" in body:
            new_mem = {
                "id": f"mem_{len(_store['memories']) + 1:03d}",
                "content": body["content"],
                "importance": body.get("importance", 0.5),
                "emotional_valence": body.get("emotional_valence", 0.0),
                "timestamp": time.time(),
                "type": body.get("type", "episodic"),
            }
            _store["memories"].append(new_mem)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps({
            "profile_id": "default",
            "memories": _store["memories"],
            "total": len(_store["memories"]),
        }).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
