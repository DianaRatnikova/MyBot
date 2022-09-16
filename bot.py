import logging
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

'''
Уровень 2
Реализуйте в боте команду /wordcount которая считает слова
в присланной фразе. Например на запрос /wordcount
Привет как дела бот должен ответить: 3 слова. Не забудьте:

Добавить проверки на пустую строку
Как можно обмануть бота, какие еще проверки нужны?
'''

# Настройки прокси
PROXY = {'proxy_url': settings.PROXY_URL,
         'urllib3_proxy_kwargs': {
                                 'username': settings.PROXY_USERNAME,
                                 'password': settings.PROXY_PASSWORD
                                 }
         }


# Записываем все сообщения в bot.log
logging.basicConfig(filename='bot.log', level=logging.INFO)


# Реакция на команду /start
def greet_user(update, context):
    update.message.reply_text('Привет! Для продолжения нажми /wordcount')


# Реакция на команду /wordcount
def ask_question(update, context):
    update.message.reply_text('Напишите предложение:')


# Функция, которая будет "отвечать" пользователю
def talk_to_me(update, context):
    if update.message.text != "":
        user_text_list = update.message.text.split()
        update.message.reply_text(f'Количество слов в данном предложении:'
                                  f'{len(user_text_list)}')
    else:
        update.message.reply_text('Вы ввели пустую строку')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", ask_question))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


main()
