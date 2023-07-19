from telebot import types

import users_google_sheet
import menu_utils
import telebot

bot = telebot.TeleBot('6045619495:AAFVbJgIXMydfgp6ZnHCRiACcNGrIhzONYs')

@bot.message_handler(commands=['start', '↩️'])
def start(message):
    id = str(message.chat.id)
    users_google_sheet.set_id(id)
    users_google_sheet.set_current_state(id, 'start')


    languages = menu_utils.get_all_languages()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for language in languages:
        markup.add(types.KeyboardButton(language))
    bot.send_message(id, 'Choose language', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in menu_utils.get_all_languages())
def select_language(message):
    id = str(message.chat.id)
    selected_language_save = message.text
    users_google_sheet.add_selected_language(id, selected_language_save)
    users_google_sheet.set_current_state(id, 'language')
    selected_language = users_google_sheet.get_selected_language(id)


    action_names = menu_utils.get_action_names_by_language(selected_language)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for action in action_names:
        markup.add(types.KeyboardButton(action))
    markup.add(types.KeyboardButton('/↩️'))

    text = menu_utils.get_message_by_key_and_language('сhoose_action', selected_language)
    bot.send_message(id, text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in menu_utils.get_all_action_names())
def select_action(message):
    id = str(message.chat.id)
    selected_action_save = message.text
    selected_language = users_google_sheet.get_selected_language(id)
    users_google_sheet.add_selected_action(id, selected_language, selected_action_save)
    users_google_sheet.set_current_state(id, 'action')
    selected_action = users_google_sheet.get_selected_action(id)


    if selected_action in menu_utils.get_all_c_and_s() or selected_action == '↩':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('↩'))
        text = menu_utils.get_message_by_key_and_language('write_complaint', selected_language)
        bot.send_message(id, text, reply_markup=markup)
        return

    category_names = menu_utils.get_category_names_by_language(selected_language)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for category in category_names:
        markup.add(types.KeyboardButton(category))
    markup.add(types.KeyboardButton('↪️'))
    text = menu_utils.get_message_by_key_and_language('сhoose_category', selected_language)
    bot.send_message(id, text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in menu_utils.get_all_category_names() or message.text == '↪️')
def select_category(message):
    id = str(message.chat.id)
    selected_language = users_google_sheet.get_selected_language(id)
    selected_action = users_google_sheet.get_selected_action(id)
    selected_category_save = message.text

    if selected_category_save == '↪️':
        message.text = selected_language
        select_language(message)
        return

    users_google_sheet.add_selected_category(id, selected_language, selected_action, selected_category_save)
    selected_category = users_google_sheet.get_selected_category(id)

    dishes_title = menu_utils.get_dishes_titles_by_category_and_language(selected_category, selected_language)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for dish_data in dishes_title:
        text = dish_data["text"]
        markup.add(types.KeyboardButton(text))
    markup.add(types.KeyboardButton('↩️'))
    text = menu_utils.get_message_by_key_and_language('choose_dish', selected_language)
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in menu_utils.get_all_titles() or message.text == '↩️')
def select_title(message):
    id = str(message.chat.id)
    selected_language = users_google_sheet.get_selected_language(id)
    selected_action = users_google_sheet.get_selected_action(id)
    selected_dish = message.text

    if selected_dish == '↩️':
        message.text = selected_action
        select_action(message)
        return

    dish_data = menu_utils.get_dish_data_by_title_and_language(selected_dish, selected_language)
    text = dish_data['text']
    image = dish_data['image']
    if image:
        bot.send_photo(message.chat.id, image, caption=text, parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, text, parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text or message.text == '↩')
def select_c_and_s(message):
    id = str(message.chat.id)
    selected_language = users_google_sheet.get_selected_language(id)

    if message.text == '↩':
        message.text = selected_language
        select_language(message)
        return

    message_c_and_s = message.from_user.first_name + ' ' + message.from_user.last_name + ' Написал(а) вам: "' + message.text + '", свяжитесь с ним/ней чтобы обсудить это.'
    bot.send_message(659863570, message_c_and_s)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('↩'))
    text = menu_utils.get_message_by_key_and_language('complaint_consideration', selected_language)
    bot.send_message(message.chat.id, text, reply_markup=markup)

bot.polling(none_stop=True)
