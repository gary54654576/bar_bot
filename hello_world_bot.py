import time
import users_google_sheet
user_data = users_google_sheet.load_data_from_google_sheets()

id = '5448502553'



def get_user_language_by_id(id):
    global row_number
    row_number = 1
    for data_tuple in user_data:
        row_number += 1
        if data_tuple[0] == id:
            user_info = data_tuple[1]
            return user_info
    return None

# Загрузите данные впервые до начала цикла
def get_user_language_info(id):
    for i in range(2):
        time.sleep(5)
        user_data = users_google_sheet.load_data_from_google_sheets()
        user_inf = get_user_language_by_id(id)
    print(user_inf)
    return user_inf
