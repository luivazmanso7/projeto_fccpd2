from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.utcnow().isoformat() + "Z"
    return jsonify(message="Servidor HTTP do desafio1 está online", timestamp=now)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

