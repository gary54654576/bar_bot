from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
import io

GOOGLE_DRIVE_CREDENTIALS_FILE = "bar-bot-telegram-7227378bbc99.json"

def get_drive_service():
    try:
        credentials = service_account.Credentials.from_service_account_file(
            GOOGLE_DRIVE_CREDENTIALS_FILE,
            scopes=["https://www.googleapis.com/auth/drive.readonly"]
        )
        with build("drive", "v3", credentials=credentials) as service:
            return service
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

def get_file_by_id(file_id):
    try:
        service = get_drive_service()
        request = service.files().get_media(fileId=file_id)
        file_content = io.BytesIO()
        downloader = MediaIoBaseDownload(file_content, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        file_content.seek(0)
        return file_content
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None
