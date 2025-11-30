from flask import Flask, jsonify

app = Flask(__name__)


USERS = [
    {"id": 1, "name": "Ana", "since": "2021-03-10"},
    {"id": 2, "name": "Bruno", "since": "2022-07-01"},
    {"id": 3, "name": "Carla", "since": "2020-11-22"},
]


@app.get("/users")
def get_users():
    return jsonify(users=USERS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

