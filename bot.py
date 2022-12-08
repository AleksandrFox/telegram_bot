from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format=u'%(asctime)s -%(levelname)s - %(message)s', # формат вывода 
                    level=logging.INFO, # что выводится 
                    filename='bot.log'  # имя файла, создается
                    )

def greet_user(update, context):
    text = 'Вызван /start'
    logging.info(text)

    update.message.reply_text(text) # ответить пользователю который написал 

def talk_to_me(update, context,):
    #user_text = f"Привет {update.message.chat.first_name}! ты написал: {update.message.text}"
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def main():
    with open('passwords.txt', 'r') as file:
        password = file.readlines()[2].strip()
    mybot = Updater(password)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info('bot starting')

    mybot.start_polling()   # начинать проверять сообщения
    mybot.idle()    # работать пока не закрыли

main()