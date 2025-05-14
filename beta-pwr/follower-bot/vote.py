# Beta Power placeholder

# Logs consumer votes for age recommendations and ad quality
import sqlite3, threading, time

conn = sqlite3.connect("beta_power.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS votes (google_id TEXT, video_id TEXT, category TEXT, score INTEGER, timestamp REAL)")
lock = threading.Lock()

def log_vote(google_id, video_id, category, score):
    # Log vote (e.g., "family", "13+", 1)
    with lock:
        cursor.execute("INSERT INTO votes (google_id, video_id, category, score, timestamp) VALUES (?, ?, ?, ?, ?)",
                      (google_id, video_id, category, score, time.time()))
        conn.commit()