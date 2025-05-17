import sqlite3
from datetime import datetime

class MessageDB:
    def __init__(self, db_path="data/messages.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender TEXT,
                message TEXT,
                timestamp TEXT
            )
        ''')
        self.conn.commit()

    def insert_message(self, sender, message):
        timestamp = datetime.utcnow().isoformat()
        self.conn.execute(
            "INSERT INTO messages (sender, message, timestamp) VALUES (?, ?, ?)",
            (sender, message, timestamp)
        )
        self.conn.commit()
