import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prompts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            score INTEGER
        );
    """)
    conn.commit()
    conn.close()

def save_prompt(text, score):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO prompts (text, score) VALUES (?, ?)", (text, score))
    conn.commit()
    conn.close()
