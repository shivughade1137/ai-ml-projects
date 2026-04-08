import sqlite3

def init_db():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        bot_response TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_chat(user, bot):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chat_logs(user_message, bot_response) VALUES (?,?)",
        (user, bot)
    )

    conn.commit()
    conn.close()