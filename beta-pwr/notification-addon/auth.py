# Google OAuth for Beta Power user authentication
from google_auth_oauthlib.flow import InstalledAppFlow
import json

def authenticate_user():
    # Authenticate with YouTube API scope
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secrets.json",
        ["https://www.googleapis.com/auth/youtube.readonly"]
    )
    credentials = flow.run_local_server()
    # Load API key from config
    with open("config.json", "r") as f:
        config = json.load(f)
    return credentials.client_id, credentials.refresh_token, config["youtube_api_key"]