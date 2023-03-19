import telebot
from telebot import types

bot = telebot.TeleBot('6045619495:AAFVbJgIXMydfgp6ZnHCRiACcNGrIhzONYs')

eng = 'English'
rus = 'Русский'
bel = 'Беларуская'

language = eng

start_command = 'start'
eng_command = 'eng'
rus_command = 'rus'
bel_command = 'bel'
menu_command = 'menu'
kitchen_command = 'kitchen'

dish_prices = [18, 22, 22, 22, 22]
dish_images = [
               "dran.jpeg",
               "doble_dran.jpeg",
               "dran_egg.jpeg",
               "dran_chiken.jpeg",
               "dran_cherry.jpeg"
               ]


def send_dishes(lang, chat_id):
    if lang == rus:
        dish_titles = [
            "Дранбургер с говядиной и сыром",
            "Двойной Дранбургер с говядиной и сыром",
            "Дранбургер с говядиной, беконом и яйцом",
            "Криспи-Дранбургер с курицей и карамелизированным луком",
            "Дымный Дранбургер с беконом и вишневым джемом"
        ]
        dish_descriptions = [
            "Драники с ароматной говядиной, сыром, зеленым салатом, томатом, маринованным огурцом и пикантным бургер-соусом.",
            "Драники с двумя порциями ароматной говядины, двойным слоем сыра, томатом, маринованным огурцом, луком, зеленым салатом и пикантным бургер-соусом.",
            "Драники с ароматной говядиной, беконом, яйцом, сыром, салатом, томатом, маринованным огурцом, луком и пикантным бургер-соусом.",
            "Драники с куриной котлетой в хрустящей панировке, сыром, салатом, томатом, маринованным огурцом, карамелизированным луком и ароматным соусом гарам масала.",
            "Драники с сочной говядиной, беконом, копченым сыром, зеленым салатом, томатом, сладким вишневым джемом и чесночным соусом."
        ]
    elif lang == bel:
        dish_titles = [
            "Дранбургер з ялавічынай і сырам",
            "Падвойны Дранбургер з ялавічынай і сырам",
            "Дранбургер з ялавічынай, беконам і яйкам",
            "Крыспі-Дранбургер з курыцай і карамелізаваным лукам",
            "Дымны Дранбургер з беконам і вішнёвым джэмам"
        ]
        dish_descriptions = [
            "Дранікі з духмянай ялавічынай, сырам, зялёнай салатай, таматам, марынаваным агурком і пікантным бургер-соусам.",
            "Дранікі з двума порцыямі духмянай ялавічыны, падвойным пластом сыра, таматам, марынаваным агурком, цыбуляй, зялёнай салатай і пікантным бургер-соусам.",
            "Дранікі з духмянай ялавічынай, беконам, яйкам, сырам, салатай, таматам, марынаваным агурком, цыбуляй і пікантным бургер-соусам.",
            "Дранікі з курынай катлетай у хрумсткай паніраванні, сырам, салатай, таматам, марынаваным агурком, карамелізаваным лукам і духмяным соусам гарам масаі.",
            "Дранікі з сакавітай ялавічынай, беконам, вэнджаным сырам, зялёнай салатай, таматам, салодкім вішнёвым джэмам і чесночным соусам."
        ]
    else:
        dish_titles = [
            "Dranburger with beef and cheese",
            "Double Dranburger with beef and cheese",
            "Dranburger with beef, bacon and egg",
            "Crispy-Dranburger with chicken and caramelized onions",
            "Smoky Dranburger with Bacon and Cherry Jam"
        ]
        dish_descriptions = [
            "Draniki with fragrant beef, cheese, green salad, tomato, pickled cucumber and spicy burger sauce.",
            "Draniki with two portions of fragrant beef, a double layer of cheese, tomato, pickled cucumber, onion, green salad and spicy burger sauce.",
            "Draniki with fragrant beef, bacon, egg, cheese, lettuce, tomato, pickled cucumber, onion and spicy burger sauce.",
            "Draniki with crispy breaded chicken cutlet, cheese, lettuce, tomato, pickled cucumber, caramelized onion and fragrant garam masala sauce.",
            "Draniki with juicy beef, bacon, smoked cheese, green salad, tomato, sweet cherry jam and garlic sauce."
        ]

    for title, description, price, image_dir in zip(dish_titles, dish_descriptions, dish_prices, dish_images):
        dish_message = f"{title} ({price} ₾)\n{description}"
        with open(image_dir, "rb") as image_file:
            bot.send_photo(chat_id, image_file, caption=dish_message)

    # Вызываем функцию start_language после вывода блюд
    start_language(chat_id)


@bot.message_handler(commands=[start_command])
def start_language(message):
    start_language(message.chat.id)


def start_language(chat_id):
    # Создаем разметку с кнопками выбора языка
    language_markup = types.InlineKeyboardMarkup()

    # Создаем кнопки для выбора языка и добавляем их в разметку
    eng_button = types.InlineKeyboardButton("eng", callback_data=eng_command)
    rus_button = types.InlineKeyboardButton("rus", callback_data=rus_command)
    bel_button = types.InlineKeyboardButton("bel", callback_data=bel_command)
    language_markup.add(eng_button, rus_button, bel_button)

    # Отправляем сообщение с выбором языка и добавляем кнопки
    bot.send_message(chat_id, "Choose language / Выберите язык / Выберыце мову", reply_markup=language_markup)


@bot.callback_query_handler(func=lambda call: call.data in [eng_command, rus_command, bel_command])
def choose_language(call):
    global language

    if call.data == eng_command:
        language = eng
    elif call.data == rus_command:
        language = rus
    elif call.data == bel_command:
        language = bel

    send_dishes(language, call.message.chat.id)
    bot.answer_callback_query(call.id)


bot.polling(none_stop=True)
