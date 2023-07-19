import gspread
from oauth2client.service_account import ServiceAccountCredentials
import menu_utils
import time


def set_id(id):
    # добавляем в гугл таблицу если ещё не добавляли
    if menu_utils.get_user_data_by_id(id) == None:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name('bar-bot-telegram-7227378bbc99.json', scope)
        client = gspread.authorize(creds)

        spreadsheet = client.open_by_url(
            'https://docs.google.com/spreadsheets/d/1x7vgXu6xrEk_Ainr7_1SKn7kQ83vryDNri0jicT14ME/edit?usp=share_link')

        sheet = spreadsheet.worksheet('user data')

        col_values = sheet.col_values(1)
        first_empty_row = len(col_values) + 1 if col_values else 1

        value = id
        if value not in col_values:
            sheet.update_cell(first_empty_row, 1, value)


def add_selected_language(id, selected_language):
    # добалвяем в гугл таблиу по id
    if menu_utils.get_user_data_by_id(id) == None:

        set_id(id)

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name('bar-bot-telegram-7227378bbc99.json', scope)
        client = gspread.authorize(creds)

        spreadsheet = client.open_by_url(
            'https://docs.google.com/spreadsheets/d/1x7vgXu6xrEk_Ainr7_1SKn7kQ83vryDNri0jicT14ME/edit?usp=share_link')

        sheet = spreadsheet.worksheet('user data')

        value = selected_language

        selected_row = menu_utils.row_number + 1

        col_values = sheet.col_values(1)
        if value not in col_values:
            sheet.update_cell(selected_row, 2, value)
    else:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name('bar-bot-telegram-7227378bbc99.json', scope)
        client = gspread.authorize(creds)

        spreadsheet = client.open_by_url(
            'https://docs.google.com/spreadsheets/d/1x7vgXu6xrEk_Ainr7_1SKn7kQ83vryDNri0jicT14ME/edit?usp=share_link')

        sheet = spreadsheet.worksheet('user data')

        value = selected_language

        selected_row = menu_utils.row_number

        col_values = sheet.col_values(1)
        if value not in col_values:
            sheet.update_cell(selected_row, 2, value)

def add_selected_action(id, selected_language, selected_action):
    if menu_utils.get_user_data_by_id(id) == None:

        add_selected_language(id, selected_language)

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('bar-bot-telegram-7227378bbc99.json', scope)
    client = gspread.authorize(creds)

    spreadsheet = client.open_by_url(
        'https://docs.google.com/spreadsheets/d/1x7vgXu6xrEk_Ainr7_1SKn7kQ83vryDNri0jicT14ME/edit?usp=share_link')

    sheet = spreadsheet.worksheet('user data')

    value = selected_action

    selected_row = menu_utils.row_number - 1

    col_values = sheet.col_values(1)
    if value not in col_values:
        sheet.update_cell(selected_row, 3, value)

def add_selected_category(id, selected_language, selected_action, selected_category):
    if menu_utils.get_user_data_by_id(id) == None:

        add_selected_action(id, selected_language, selected_action)

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('bar-bot-telegram-7227378bbc99.json', scope)
    client = gspread.authorize(creds)

    spreadsheet = client.open_by_url(
        'https://docs.google.com/spreadsheets/d/1x7vgXu6xrEk_Ainr7_1SKn7kQ83vryDNri0jicT14ME/edit?usp=share_link')

    sheet = spreadsheet.worksheet('user data')

    value = selected_category

    selected_row = menu_utils.row_number - 1

    col_values = sheet.col_values(1)
    if value not in col_values:
        sheet.update_cell(selected_row, 4, value)

def set_current_state(id, current_state):
    # записываем послединй выбранный пункт меню
    if menu_utils.get_user_data_by_id(id) == None:

        set_id(id)

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name('bar-bot-telegram-7227378bbc99.json', scope)
        client = gspread.authorize(creds)

        spreadsheet = client.open_by_url(
            'https://docs.google.com/spreadsheets/d/1x7vgXu6xrEk_Ainr7_1SKn7kQ83vryDNri0jicT14ME/edit?usp=share_link')

        sheet = spreadsheet.worksheet('user data')

        value = current_state

        selected_row = menu_utils.row_number + 1

        col_values = sheet.col_values(1)
        if value not in col_values:
            sheet.update_cell(selected_row, 5, value)
    else:
        set_id(id)

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name('bar-bot-telegram-7227378bbc99.json', scope)
        client = gspread.authorize(creds)

        spreadsheet = client.open_by_url(
            'https://docs.google.com/spreadsheets/d/1x7vgXu6xrEk_Ainr7_1SKn7kQ83vryDNri0jicT14ME/edit?usp=share_link')

        sheet = spreadsheet.worksheet('user data')

        value = current_state
        if value == 'start' or value == 'language':
            selected_row = menu_utils.row_number
        else:
            selected_row = menu_utils.row_number - 1

        col_values = sheet.col_values(1)
        if value not in col_values:
            sheet.update_cell(selected_row, 5, value)

def get_selected_language(id):

    menu_utils.user_data = load_data_from_google_sheets()
    user_info = menu_utils.get_user_language_by_id(id)
    return user_info

def get_selected_action(id):
    # ищем по id выбранное действие в таблице и возвращаем его

    menu_utils.user_data = load_data_from_google_sheets()
    user_info = menu_utils.get_user_action_by_id(id)
    return user_info

def get_selected_category(id):
    # ищем по id выбранную категорию в таблице и возвращаем её

    menu_utils.user_data = load_data_from_google_sheets()
    user_info = menu_utils.get_user_category_by_id(id)
    return user_info


def load_data_from_google_sheets():

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('bar-bot-telegram-7227378bbc99.json', scope)
    client = gspread.authorize(creds)

    spreadsheet = client.open_by_url(
        'https://docs.google.com/spreadsheets/d/1x7vgXu6xrEk_Ainr7_1SKn7kQ83vryDNri0jicT14ME/edit?usp=share_link')

    sheet = spreadsheet.worksheet('user data')

    # Получите все значения из этого листа
    values = sheet.get_all_values()

    return values

