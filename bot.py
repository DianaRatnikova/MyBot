
import logging
import settings # для файла settings.py (типа include в си)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# Updater - коммуникация с сервером (получает/передает сообщения)
# CommandHandler - обработчик команд
# MessageHandler - обработчик текстовых сообщений
# Filters




# Настройки прокси
#PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
#    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

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
    print('Вызван /start:')
    update.message.reply_text('Привет, пользователь!) Ты вызвал команду /start')

# Функция, которая будет "отвечать" пользователю
def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)


# Функция, кот соединяется с Telegram, "тело" бота
def main():
    print('Hello')
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    #mybot = Updater("5538006894:AAGSXUXLMpYUKQW87dJ0W83gFfu7swoDc6A", use_context=True, request_kwargs=PROXY)
    #mybot = Updater("5538006894:AAGSXUXLMpYUKQW87dJ0W83gFfu7swoDc6A", use_context=True)
    mybot = Updater(settings.API_KEY, use_context=True)

# Диспетчер нужен, чтобы при наступлении события вызывалась функция:
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user)) #без слэша
# Хотим реагировать только на текстовые сообщения  - Filters.text
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) 

    #Залогируем в файл информацию о старте бота
    logging.info("Бот стартовал / Bot started")

    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

main()

