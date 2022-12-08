from ast import parse
import telebot

import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('Pictures//welcome.mp4', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}</b>, бот созданный чтобы на мне учились'.format(message.from_user, bot.get_me()),
    parse_mode='html')

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)

# RUN
bot.polling(none_stop=True) 