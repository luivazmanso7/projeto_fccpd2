import os
from datetime import datetime

from flask import Flask, jsonify
import psycopg2
import redis

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        port=int(os.environ.get("DB_PORT", "5432")),
        user=os.environ.get("DB_USER", "app"),
        password=os.environ.get("DB_PASSWORD", "app"),
        dbname=os.environ.get("DB_NAME", "appdb"),
    )
    return conn


def get_redis_client():
    client = redis.Redis(
        host=os.environ.get("CACHE_HOST", "cache"),
        port=int(os.environ.get("CACHE_PORT", "6379")),
        db=0,
    )
    return client


@app.route("/")
def index():
    now = datetime.utcnow().isoformat() + "Z"

    # Postgres: garantir tabela e registrar acesso
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS access_log (
                    id SERIAL PRIMARY KEY,
                    created_at TIMESTAMPTZ NOT NULL,
                    note TEXT NOT NULL
                )
                """
            )
            cur.execute(
                "INSERT INTO access_log (created_at, note) VALUES (NOW(), %s)",
                ("Acesso via endpoint raiz",),
            )
            conn.commit()
    finally:
        conn.close()

    # Redis: contador de acessos
    cache = get_redis_client()
    total_hits = cache.incr("web_hits")

    return jsonify(
        message="Aplicação do desafio3 em execução",
        timestamp=now,
        total_hits=int(total_hits),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

