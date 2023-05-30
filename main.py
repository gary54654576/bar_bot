from telebot import types
import telebot

from menu_utils import get_all_languages
from menu_utils import get_all_category_names
from menu_utils import get_category_names_by_and_language
from menu_utils import get_dishes_data_by_category
from menu_utils import get_message_by_key_and_language

bot = telebot.TeleBot('6277113813:AAH4cEoCB_kStfhSHO4JUiawhkRKlw3K_LQ')
@bot.message_handler(commands=['start', '🔙'])
def start(message):
    languages = get_all_languages()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for language in languages:
        markup.add(types.KeyboardButton(language))
    bot.send_message(message.chat.id, 'Choose language', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in get_all_languages())
def select_language(message):
    global selected_language
    selected_language = message.text

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    category_names = get_category_names_by_and_language(selected_language)
    for category in category_names:
        markup.add(types.KeyboardButton(category))
    markup.add(types.KeyboardButton('/🔙'))

    text = get_message_by_key_and_language('сhoose_category', selected_language)
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in get_all_category_names())
def select_category(message):
    selected_category = message.text
    dishes_data = get_dishes_data_by_category(selected_category, selected_language)
    for dish_data in dishes_data:
        text = dish_data["text"]
        image = dish_data["image"]
        if image:
            bot.send_photo(message.chat.id, image, caption=text, parse_mode='HTML')
        else:
            bot.send_message(message.chat.id, text, parse_mode='HTML')

bot.polling(none_stop=True)