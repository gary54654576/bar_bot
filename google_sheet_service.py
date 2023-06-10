from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

GOOGLE_DRIVE_CREDENTIALS_FILE = "bar-bot-telegram-7227378bbc99.json"
SPREADSHEET_ID = '1x7vgXu6xrEk_Ainr7_1SKn7kQ83vryDNri0jicT14ME'

def get_drive_service():
    try:
        credentials = service_account.Credentials.from_service_account_file(
            GOOGLE_DRIVE_CREDENTIALS_FILE,
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
        with build("sheets", "v4", credentials=credentials) as service:
            return service
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

def get_languages():
    LANGUAGES_RANGE = 'languages!B2:B'
    service = get_drive_service()
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=LANGUAGES_RANGE).execute()
    languages = result.get('values', [])
    return [language[0] for language in languages]

def get_messages():
    MESSAGES_RANGE = 'messages!A2:D'
    service = get_drive_service()
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=MESSAGES_RANGE).execute()
    messages = result.get('values', [])
    return messages

def get_menu_categories():
    CATEGORIES_RANGE = 'menu buttons!A2:A'
    service = get_drive_service()
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=CATEGORIES_RANGE).execute()
    categories = result.get('values', [])
    return [category[0] for category in categories]

def get_common_data():
    COMMON_DATA_RANGE = 'common!A2:D'
    service = get_drive_service()
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=COMMON_DATA_RANGE).execute()
    common_data = result.get('values', [])
    return common_data

def get_titles():
    TITLES_RANGE = 'titles!A2:D'
    service = get_drive_service()
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=TITLES_RANGE).execute()
    titles = result.get('values', [])
    return titles

def get_descriptions():
    DESCRIPTIONS_RANGE = 'descriptions!A2:D'
    service = get_drive_service()
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=DESCRIPTIONS_RANGE).execute()
    descriptions = result.get('values', [])
    return descriptions

def get_menu_category_button_names():
    BUTTONS_RANGE = 'menu buttons!A2:D'
    service = get_drive_service()
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=BUTTONS_RANGE).execute()
    buttons = result.get('values', [])
    return buttons

def get_action_button_names():
    BUTTONS_RANGE = 'action buttons!A2:D'
    service = get_drive_service()
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=BUTTONS_RANGE).execute()
    buttons = result.get('values', [])
    return buttons

def get_c_and_s():
    BUTTONS_RANGE = 'action buttons!A3:D'
    service = get_drive_service()
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=BUTTONS_RANGE).execute()
    buttons = result.get('values', [])
    return buttons[0]
