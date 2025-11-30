import os

import requests
from flask import Flask, jsonify

app = Flask(__name__)


USERS_SERVICE_URL = os.environ.get("USERS_SERVICE_URL", "http://users-service:5000")
ORDERS_SERVICE_URL = os.environ.get("ORDERS_SERVICE_URL", "http://orders-service:5001")


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/users")
def proxy_users():
    response = requests.get(f"{USERS_SERVICE_URL}/users", timeout=5)
    response.raise_for_status()
    return jsonify(response.json())


@app.get("/orders")
def proxy_orders():
    response = requests.get(f"{ORDERS_SERVICE_URL}/orders", timeout=5)
    response.raise_for_status()
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

