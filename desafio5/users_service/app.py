from flask import Flask, jsonify

app = Flask(__name__)


USERS = [
    {"id": 1, "name": "Ana"},
    {"id": 2, "name": "Bruno"},
    {"id": 3, "name": "Carla"},
]


@app.get("/users")
def get_users():
    return jsonify(users=USERS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

