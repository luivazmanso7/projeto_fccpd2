from flask import Flask, jsonify

app = Flask(__name__)


ORDERS = [
    {"id": 1, "user_id": 1, "total": 150.0},
    {"id": 2, "user_id": 2, "total": 230.5},
    {"id": 3, "user_id": 1, "total": 89.9},
]


@app.get("/orders")
def get_orders():
    return jsonify(orders=ORDERS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

