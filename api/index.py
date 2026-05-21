"""KAGUYA API — Vercel Serverless Function."""
from http.server import BaseHTTPRequestHandler
import json


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        response = {
            "name": "KAGUYA — AI Personality Engine",
            "version": "0.2.0",
            "docs": "/api/docs",
            "endpoints": {
                "health": "/api/health",
                "personality": "/api/personality",
                "emotion": "/api/emotion",
                "chat": "/api/chat",
                "relationships": "/api/relationships",
                "memory": "/api/memory",
            },
        }
        self.wfile.write(json.dumps(response).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
