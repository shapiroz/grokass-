# Backend for YouTube API integration and ad tagging
import googleapiclient.discovery
import json

# Load API key
with open("../config.json", "r") as f:
    config = json.load(f)
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=config["youtube_api_key"])

def fetch_videos():
    request = youtube.videos().list(part="snippet", chart="mostPopular", maxResults=10)
    response = request.execute()
    return response["items"]

def tag_ad(video_id):
    return {"video_id": video_id, "is_ad": False}