import google_sheet_service
import google_drive_service
from importlib import reload
import sys


# Перезагрузка модуля google_sheet_service
reload(sys.modules['google_sheet_service'])

user_data = google_sheet_service.get_user_data()
languages = google_sheet_service.get_languages()
messages = google_sheet_service.get_messages()
categories = google_sheet_service.get_menu_categories()
common_data = google_sheet_service.get_common_data()
titles = google_sheet_service.get_titles()
descriptions = google_sheet_service.get_descriptions()
category_button_names = google_sheet_service.get_menu_category_button_names()
action_buttons = google_sheet_service.get_action_button_names()
c_and_s = google_sheet_service.get_c_and_s()

# -------------------------------------------------------------
# Импортируемые функции
# -------------------------------------------------------------

def get_user_data_by_id(id):
    global row_number
    row_number = 1
    for data_tuple in user_data:
        row_number += 1
        if data_tuple[0] == id:
            user_info = data_tuple
            return user_info
    return None

def get_user_language_by_id(id):
    global row_number
    row_number = 1
    for data_tuple in user_data:
        row_number += 1
        if data_tuple[0] == id:
            user_info = data_tuple[1]
            return user_info
    return None


def get_user_action_by_id(id):
    global row_number
    row_number = 1
    for data_tuple in user_data:
        row_number += 1
        if data_tuple[0] == id:
            user_info = data_tuple[2]
            return user_info
    return None

def get_user_category_by_id(id):
    global row_number
    row_number = 1
    for data_tuple in user_data:
        row_number += 1
        if data_tuple[0] == id:
            user_info = data_tuple[3]
            return user_info
    return None

def get_user_current_state_by_id(id):
    global row_number
    row_number = 1
    for data_tuple in user_data:
        row_number += 1
        if data_tuple[0] == id:
            user_info = data_tuple[4]
            return user_info
    return None


def quantity_test(arr, i):
    try:
        value = arr[i]
        return 0
    except IndexError:
        return 1


def get_all_category_names():
    category_names = []
    for category in category_button_names:
        category_names.extend(category[1:])
    return category_names

def get_all_action_names():
    action_names = []
    for action in action_buttons:
        action_names.extend(action[1:])
    return action_names

def get_all_c_and_s():
    return c_and_s

def get_all_languages():
    return languages

def get_all_titles():
    dish_title = []
    for title in titles:
        dish_title.extend(title[1:])
    return dish_title

def get_dish_data_by_title_and_language(dish_name, language):
    title = get_selected_title_by_name(dish_name)
    key = get_key_for_title(title, common_data)
    data = get_data_by_key_and_language(key, language)
    if data:
        for item in data:
            message_text = f'<b>{item["title"]}</b>\n'
            message_text += f'{item["description"]}\n'
            message_text += f'<b>{item["price"]}</b>\n'
            image_id = item["image_id"]
            if image_id != '' and image_id != None:
                image_file = google_drive_service.get_file_by_id(image_id)
                dish_data = {
                    'text': message_text,
                    'image': image_file
                }
                data = dish_data
            else:
                dish_data = {
                    'text': message_text,
                    'image': None
                }
                data = dish_data
    return data

def get_dishes_titles_by_category_and_language(category_name, language):
    category = get_selected_category_by_name(category_name)
    keys = get_keys_for_category(category, common_data)
    data = get_titles_by_keys_and_language(keys, language)
    dishes_data = []
    if data:
        for item in data:
            message_text = f'{item["title"]}'
            dish_data = {
                'text': message_text
            }
            dishes_data.append(dish_data)
    return dishes_data

def get_language_indexes():
    language_indexes = {}
    for i, language in enumerate(languages, start=1):
        language_indexes[language] = i
    return language_indexes

def get_language_index(language):
    language_indexes = get_language_indexes()
    if language not in language_indexes:
        return None
    return language_indexes[language]

def get_message_by_key_and_language(key, language):
    for message_tuple in messages:
        if message_tuple[0] == key:
            language_index = get_language_index(language)
            message = message_tuple[language_index]
            return message
    return None

def get_category_names_by_language(language):
    index = get_language_index(language)
    names = []
    for category_names in category_button_names:
        names.append(category_names[index])
    return names

def get_action_names_by_language(language):
    index = get_language_index(language)
    names = []
    for action_button in action_buttons:
        names.append(action_button[index])
    return names

def get_dish_names_by_language(language):
    index = get_language_index(language)
    names = []
    for dish_names in titles:
        names.append(dish_names[index])
    return names

def get_selected_category_by_name(category_name):
    for category_names in category_button_names:
        if category_name in category_names:
            return category_names[0]
    return None

def get_selected_title_by_name(dish_name):

    for dish_names in titles:
        if dish_name in dish_names:
            return dish_names[0]
    return None

def get_selected_action_by_name(action_name):

    for action_names in action_buttons:
        if action_name in action_names:
            return action_names[0]
    return None

# -------------------------------------------------------------
# Неимпортируемые функции
# -------------------------------------------------------------
def get_keys_for_category(category, common_data):
    keys_for_category = []

    for row in common_data:
        if row[-1] == category:
            keys_for_category.append(row[0])

    return keys_for_category

def get_key_for_title(title, common_data):
    key_for_title = None
    for row in common_data:
        if row[0] == title:
            key_for_title = row[0]

    return key_for_title

def get_title_by_key_and_language(key, language):
    index = get_language_index(language)

    for title_tuple in titles:
        if title_tuple[0] == key:
            title = title_tuple[index]
            return title


    return None

def get_description_by_key_and_language(key, language):
    index = get_language_index(language)

    for description_tuple in descriptions:
        if description_tuple[0] == key:
            description = description_tuple[index]
            return description

    return None

def get_price_and_image_id_by_key(key, common_data):
    for row in common_data:
        if row[0] == key:
            price = row[1]
            image_id = row[2]

            return price, image_id

    return None, None

def get_titles_by_keys_and_language(keys, language):
    result_data = []

    for key in keys:
        title = get_title_by_key_and_language(key, language)

        if title:
            data = {
                'title': title
            }
            result_data.append(data)

    return result_data

def get_data_by_key_and_language(key, language):
    result_data = []
    title = get_title_by_key_and_language(key, language)
    description = get_description_by_key_and_language(key, language)
    price, image_id = get_price_and_image_id_by_key(key, common_data)


    if title and description and price:
        data = {
            'key': key,
            'title': title,
            'description': description,
            'price': price,
            'image_id': image_id
        }
        result_data.append(data)

    return result_data




