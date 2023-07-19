import gspread
from oauth2client.service_account import ServiceAccountCredentials

def write_id_to_gsheet(list_of_values):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    # используйте json файл, который вы получили при создании сервисного аккаунта
    creds = ServiceAccountCredentials.from_json_keyfile_name('bar-bot-telegram-7227378bbc99.json', scope)
    client = gspread.authorize(creds)

    # откройте таблицу по ее имени
    spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1x7vgXu6xrEk_Ainr7_1SKn7kQ83vryDNri0jicT14ME/edit?usp=share_link')

    sheet = spreadsheet.worksheet('user data')

    # Определяем первую пустую строку в столбце
    col_values = sheet.col_values(1)  # Измените номер столбца при необходимости
    first_empty_row = len(col_values) + 1 if col_values else 1

    # Записываем данные в каждую пустую строку
    for i, value in enumerate(list_of_values, start=first_empty_row):
        if value not in col_values:
            sheet.update_cell(i, 1, value)  # Измените номер столбца при необходимости

def write_to_gsheet(list_of_values, column_number):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    # используйте json файл, который вы получили при создании сервисного аккаунта
    creds = ServiceAccountCredentials.from_json_keyfile_name('bar-bot-telegram-7227378bbc99.json', scope)
    client = gspread.authorize(creds)

    # откройте таблицу по ее имени
    spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1x7vgXu6xrEk_Ainr7_1SKn7kQ83vryDNri0jicT14ME/edit?usp=share_link')

    sheet = spreadsheet.worksheet('user_data')



    # Записываем данные в каждую пустую строку
    for i, value in enumerate(list_of_values, start=2):
        sheet.update_cell(i, column_number, value)  # Измените номер столбца при необходимости


