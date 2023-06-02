import telebot
bot = telebot.TeleBot('6098199640:AAG2n_VDMk5J-0btXrGji2Uvpwla3aoRx2E')
print(1)
@bot.message_handler(commands=['start'])
def start(message):
    print(2)
    bot.send_message(message.chat.id, "hello world")

print(3)
bot.polling(none_stop=True)