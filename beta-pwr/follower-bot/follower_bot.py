# Tracks YouTube actions for consumer reputation signatures
import googleapiclient.discovery
import threading, sqlite3, time, json

# Load API key
with open("../config.json", "r") as f:
    config = json.load(f)
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=config["youtube_api_key"])
conn = sqlite3.connect("beta_power.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS actions (google_id TEXT, video_id TEXT, action TEXT, timestamp REAL)")
lock = threading.Lock()

def track_action(google_id, video_id, action):
    with lock:
        cursor.execute("INSERT INTO actions (google_id, video_id, action, timestamp) VALUES (?, ?, ?, ?)",
                      (google_id, video_id, action, time.time()))
        conn.commit()

def track_video(google_id, video_id):
    track_action(google_id, video_id, "watch")