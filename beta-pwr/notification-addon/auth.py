# Beta Power placeholder
# Google OAuth for Beta Power user authentication
from google_auth_oauthlib.flow import InstalledAppFlow

def authenticate_user():
    # Authenticate with YouTube API scope
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secrets.json",
        ["https://www.googleapis.com/auth/youtube.readonly"]
    )
    credentials = flow.run_local_server()
    return credentials.client_id, credentials.refresh_token
