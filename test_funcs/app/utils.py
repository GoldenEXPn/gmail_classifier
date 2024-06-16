import os
import pickle
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_flow():
    return Flow.from_client_secrets_file(
        'credentials.json',
        scopes=SCOPES,
        redirect_uri='http://localhost:5000/callback'
    )

def save_credentials(user_id, credentials):
    with open(f'token_{user_id}.pickle', 'wb') as token:
        pickle.dump(credentials, token)

def load_credentials(user_id):
    if os.path.exists(f'token_{user_id}.pickle'):
        with open(f'token_{user_id}.pickle', 'rb') as token:
            credentials = pickle.load(token)
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            return credentials
    return None
