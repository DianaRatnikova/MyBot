import logging
import settings
from datetime import datetime
import ephem
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
    update.message.reply_text(f'Привет! Выбери из меню:'
                              f'\n/wordcount - подсчитать количество слов в предложении'
                              f'\n/next_full_moon - узнать дату ближайшего полнолуния')


# Реакция на команду /wordcount
def request_a_sentence(update, context):
    update.message.reply_text('Напишите предложение:')


def check_if_string_is_ok(list_of_words_from_user):
    string_is_ok = True
    for word in list_of_words_from_user:
        if not word.isalpha():
            string_is_ok = False
    return string_is_ok


# Функция, которая будет "отвечать" пользователю
def count_and_show_number_of_words(update, context):
    if update.message.text:
        user_text_list = update.message.text.split()
        if check_if_string_is_ok(user_text_list):
            update.message.reply_text(f'Количество слов в данном предложении: '
                                      f'{len(user_text_list)}')
        else:
            update.message.reply_text('Вы ввели плохую строку')
    else:
        update.message.reply_text('Вы ввели пустую строку')


def show_date_of_full_moon(update, context):
    date_of_full_moon = ephem.next_full_moon(datetime.now())
    update.message.reply_text(f'Ближайшее полнолуние {date_of_full_moon}')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", request_a_sentence))
    dp.add_handler(CommandHandler("next_full_moon", show_date_of_full_moon))
    dp.add_handler(MessageHandler(Filters.text, count_and_show_number_of_words))
    mybot.start_polling()
    mybot.idle()


main()
