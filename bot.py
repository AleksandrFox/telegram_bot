import telebot
import random
from telebot import types
from glob import glob

import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['help'])
def ansver_help(message):
    stic_help = open('Pictures//AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, stic_help)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('Pictures//welcome1.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

# Keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Мотоцикл')
    item2 = types.KeyboardButton('Как дела?')
    item3 = types.KeyboardButton('Бот йобаный!!!')

    markup.add(item1, item2, item3)

    mess = f'Добро пожаловать! <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

def send_moto_picture(message):
    moto_list = glob('Pictures//moto*.jp*g')
    moto_pic = random.choice(moto_list)
    bot.send_photo(message.chat.id, photo=open(moto_pic, 'rb'))

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        stic_eba = open('Pictures//sticker12.webp', 'rb')
        if message.text == 'Мотоцикл':
            send_moto_picture(message)
        elif message.text == 'Как дела?':
            bot.send_message(message.chat.id, 'Отлично, как сам?')
        elif message.text == 'Бот йобаный!!!':
            bot.send_sticker(message.chat.id, stic_eba)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить...')

# RUN
bot.polling(none_stop=True) 