import telebot
import menu_utils
from importlib import reload  # Добавлено для перезагрузки модуля
import sys

from telebot import types

# Перезагрузка модуля menu_utils
reload(sys.modules['menu_utils'])

bot = telebot.TeleBot('6045619495:AAFVbJgIXMydfgp6ZnHCRiACcNGrIhzONYs')

@bot.message_handler(commands=['start', '↩️'])
def start(message):
    print('start def "start"')
    global user_id
    user_id = message.chat.id
    languages = menu_utils.get_all_languages()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for language in languages:
        markup.add(types.KeyboardButton(language))
    bot.send_message(user_id, 'Choose language', reply_markup=markup)
    print('finish def "start"')

@bot.message_handler(func=lambda message: message.text in menu_utils.get_all_languages())
def select_language(message):
    print('start def "select_language"')
    global select_language_message
    select_language_message = message
    global selected_language
    selected_language = message.text
    action_names = menu_utils.get_action_names_by_language(selected_language)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for action in action_names:
        markup.add(types.KeyboardButton(action))
    markup.add(types.KeyboardButton('/↩️'))
    text = menu_utils.get_message_by_key_and_language('сhoose_action', selected_language)
    bot.send_message(user_id, text, reply_markup=markup)
    print('finish def "select_language"')

@bot.message_handler(func=lambda message: message.text in menu_utils.get_all_action_names() or message.text == '↩️')
def select_action(message):
    print('start def "select_action"')
    global selected_action_message
    selected_action_message = message
    global selected_action
    selected_action = message.text
    if selected_action in menu_utils.get_all_c_and_s() or selected_action == '↩':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('↩'))
        text = menu_utils.get_message_by_key_and_language('write_complaint', selected_language)
        bot.send_message(user_id, text, reply_markup=markup)
        return
    category_names = menu_utils.get_category_names_by_language(selected_language)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for category in category_names:
        markup.add(types.KeyboardButton(category))
    markup.add(types.KeyboardButton('↪️'))
    text = menu_utils.get_message_by_key_and_language('сhoose_category', selected_language)
    bot.send_message(user_id, text, reply_markup=markup)
    print('finish def "select_action"')

@bot.message_handler(func=lambda message: message.text in menu_utils.get_all_category_names() or message.text == '↪️')
def select_category(message):
    print('start def "select_category"')
    global selected_category
    selected_category = message.text
    if selected_category == '↪️':
        select_language(select_language_message)
        return
    dishes_title = menu_utils.get_dishes_titles_by_category_and_language(selected_category, selected_language)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for dish_data in dishes_title:
        text = dish_data["text"]
        markup.add(types.KeyboardButton(text))
    markup.add(types.KeyboardButton('↩️'))
    text = menu_utils.get_message_by_key_and_language('choose_dish', selected_language)
    bot.send_message(user_id, text, reply_markup=markup)
    print('finish def "select_category"')

@bot.message_handler(func=lambda message: message.text in menu_utils.get_all_titles() or message.text == '↩️')
def select_title(message):
    print('start def "select_title"')
    selected_dish = message.text
    if selected_dish == '↩️':
        select_action(selected_action_message)
        return
    dish_data = menu_utils.get_dish_data_by_title_and_language(selected_dish, selected_language)
    text = dish_data['text']
    image = dish_data['image']
    if image:
        bot.send_photo(user_id, image, caption=text, parse_mode='HTML')
    else:
        bot.send_message(user_id, text, parse_mode='HTML')
    print('finish def "select_title"')

@bot.message_handler(func=lambda message: message.text or message.text == '↩')
def select_c_and_s(message):
    print('start def "select_c_and_s"')
    selected_c_and_s = message.text
    if selected_c_and_s == '↩':
        select_language(select_language_message)
        return
    message_c_and_s = message.from_user.first_name + ' ' + message.from_user.last_name + ' Написал(а) вам: "' + message.text + '", свяжитесь с ним/ней чтобы обсудить это.'
    bot.send_message(659863570, message_c_and_s)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('↩'))
    text = menu_utils.get_message_by_key_and_language('complaint_consideration', selected_language)
    bot.send_message(user_id, text, reply_markup=markup)
    print('finish def "select_c_and_s"')

bot.polling(none_stop=True)
