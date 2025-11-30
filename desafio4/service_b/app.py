import os

import requests
from flask import Flask, jsonify

app = Flask(__name__)


SERVICE_A_HOST = os.environ.get("SERVICE_A_HOST", "service-a")
SERVICE_A_PORT = os.environ.get("SERVICE_A_PORT", "5000")


def fetch_users():
    url = f"http://{SERVICE_A_HOST}:{SERVICE_A_PORT}/users"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    return data.get("users", [])


@app.get("/status")
def status():
    return jsonify(ok=True)


@app.get("/report")
def report():
    users = fetch_users()
    enriched = [
        {
            "message": f"Usuário {u['name']} ativo desde {u['since']}",
            "id": u["id"],
        }
        for u in users
    ]
    return jsonify(report=enriched)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

