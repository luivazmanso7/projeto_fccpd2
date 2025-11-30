import os
import sqlite3
from datetime import datetime

DB_PATH = os.environ.get("DB_PATH", "/data/desafio2.sqlite")


def init_db(conn):
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            description TEXT NOT NULL
        )
        """
    )
    conn.commit()


def insert_event(conn, description: str):
    conn.execute(
        "INSERT INTO events (created_at, description) VALUES (?, ?)",
        (datetime.utcnow().isoformat() + "Z", description),
    )
    conn.commit()


def list_events(conn):
    cursor = conn.execute("SELECT id, created_at, description FROM events ORDER BY id")
    return cursor.fetchall()


def main():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    print(f"Usando banco de dados em: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    try:
        init_db(conn)
        insert_event(conn, "Execução da aplicação de exemplo")
        events = list_events(conn)

        print("Eventos armazenados:")
        for event_id, created_at, description in events:
            print(f"- #{event_id} | {created_at} | {description}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()

