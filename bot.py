from telegram.ext import Updater, CommandHandler

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def greet_user(update, context):
    print('Вызван /start:')
    update.message.reply_text('Привет, пользователь!) Ты вызвал команду /start')
    

def main():
    print('Hello')
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    #mybot = Updater("5538006894:AAGSXUXLMpYUKQW87dJ0W83gFfu7swoDc6A", use_context=True, request_kwargs=PROXY)
    mybot = Updater("5538006894:AAGSXUXLMpYUKQW87dJ0W83gFfu7swoDc6A", use_context=True)


    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user)) #без слэша

    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

main()

